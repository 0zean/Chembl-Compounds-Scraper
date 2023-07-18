from scraper import setup_browser, retrieve_compound_data

# Setup the custom browser
browser = setup_browser('209.182.236.218:5901')

# Retrieve the compounds
retrieve_compound_data(browser, 'nandrolone')

browser.quit()
