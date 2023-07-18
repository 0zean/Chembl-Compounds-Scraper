import base64
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait


# Find the downloads on remote driver
def get_downloaded_files(driver):
    if not driver.current_url.startswith("chrome://downloads"):
        driver.get("chrome://downloads/")

    return driver.execute_script(
        "return  document.querySelector('downloads-manager')  "
        " .shadowRoot.querySelector('#downloadsList')         "
        " .items.filter(e => e.state === 'COMPLETE')          "
        " .map(e => e.filePath || e.file_path || e.fileUrl || e.file_url); "
    )


# Get the actual zipfile to save
def get_file_content(driver, path):
    elem = driver.execute_script(
        "var input = window.document.createElement('INPUT'); "
        "input.setAttribute('type', 'file'); "
        "input.hidden = true; "
        "input.onchange = function (e) { e.stopPropagation() }; "
        "return window.document.documentElement.appendChild(input); "
    )

    elem._execute("sendKeysToElement", {"value": [path], "text": path})

    result = driver.execute_async_script(
        "var input = arguments[0], callback = arguments[1]; "
        "var reader = new FileReader(); "
        "reader.onload = function (ev) { callback(reader.result) }; "
        "reader.onerror = function (ex) { callback(ex.message) }; "
        "reader.readAsDataURL(input.files[0]); "
        "input.remove(); ",
        elem,
    )

    if not result.startswith("data:"):
        raise Exception("Failed to get file content: %s" % result)

    return base64.b64decode(result[result.find("base64,") + 7 :])


# Setup browser
def setup_browser(url: str, download_path=os.getcwd() + "/data/chembl_compounds"):
    # instantiate the options class
    options = webdriver.ChromeOptions()
    options.set_capability("browserName", "chrome")
    
    # Add arguments: download_path
    options.add_experimental_option(
        "prefs",
        {
            "download.prompt_for_download": False,
            # "download.directory_upgrade": True,
            # "safebrowsing.enabled": False,
        },
    )

    # Remote Chrome Host
    browser = webdriver.Remote(url, options=options)

    return browser


# Navigate to the compounds endpoint of a specific compound
def retrieve_compound_data(browser, compound_name: str):
    
    # driver settings
    browser.maximize_window()
    browser.implicitly_wait(100)
    
    # Unique compound URL
    url = f"https://www.ebi.ac.uk/chembl/g/#search_results/compounds/query={compound_name}"

    # Navigate to the above URL
    browser.get(url)

    # Explicit waiting
    # wait = WebDriverWait(browser, 100)
    # csv_button = wait.until(
    #     EC.element_to_be_clickable(
    #         (By.XPATH,
    #         '//*[@id="BCK-ESCompound-container"]/div/div[2]/div[1]/div[3]/div/a[1]',
    #             )
    #         )
    #     )

    # Find the CSV button
    csv_button = browser.find_element(
                By.XPATH,
                '//*[@id="BCK-ESCompound-container"]/div/div[2]/div[1]/div[3]/div/a[1]',
            )
    csv_button.click()

    # Download hyperlink
    download_button = browser.find_element(
                By.XPATH,
                '//*[@id="BCK-ESCompound-container"]/div/div[2]/div[2]/div/div/div[4]/a[1]',
            )
    
    download_button.click()

    # sleep(5)

    # list all the completed remote files (waits for at least one)
    # files = WebDriverWait(browser, 20, 1).until(get_downloaded_files)
    files = get_downloaded_files(browser)

    # get the content of the first file remotely
    content = get_file_content(browser, files[0])

    # save the content in a local file in the working directory
    path = os.getcwd() + "/data/chembl_compounds/"
    if files is not None:
        with open(path + os.path.basename(files[0]), "wb") as f:
            f.write(content)
    os.rename(path + os.path.basename(files[0]), f"{path}/{compound_name}.zip")

    sleep(3)
