# Chembl UK Web Scraper and Molecular Visualization Pipeline

# Overview
This project consists of a web scraper built with Selenium that extracts compound data from the Chembl UK website. It retrieves information such as compound names, molecular formulas, SMILES strings, and other relevant data. The scraped data is collected in a CSV format. Additionally, the project includes a Dockerized and deployed remote Selenium instance to enhance accessibility for scraping compound data from the Chembl UK database.

Furthermore, microservices have been created using MageAI for various tasks such as unzipping, consolidating, and loading the scraped data into a PostgreSQL database. This ensures efficient data management and organization.

To provide users with a visual representation of the compounds, a pipeline has been developed for generating two-dimensional molecular visualizations. This pipeline utilizes RDKit, a cheminformatics library, to create visualizations based on the SMILES string data obtained from the PostgreSQL database. Users can quickly analyze and gain insights into the molecular structure of the compounds.


Caffeine                                  |  Metformin
:----------------------------------------:|:-----------------------------------------:
![alt text](data/molecules/CAFFEINE.png)  |  ![alt text](data/molecules/METFORMIN.png)


# Features
- Web scraper using Selenium to extract compound data from the Chembl UK website.
Dockerized and deployed remote Selenium instance for improved accessibility.
- Microservices implemented in MageAI for unzipping, consolidating, and loading data into a PostgreSQL database.
- Pipeline for generating two-dimensional molecular visualizations using RDKit and SMILES string data.

# Installation
To run this project locally, follow these steps:

Clone the repository:

```bash
git clone https://github.com/0zean/Chembl-Compounds-Scraper.git
```
Install the required dependencies:
```bash
pip install -r requirements.txt
```

Set up and configure Docker for running the remote Selenium instance. Refer to the Docker documentation for instructions specific to your operating system.

Set up the PostgreSQL database and ensure it is running correctly. Update the database connection settings in the project configuration files accordingly.

# Usage
Update the `credentials.yaml` file to your own PostgreSQL credentials.

Launch the web scraper by running the following command:
```bash
python scrape_compound.py
```

Run the molecular visualization pipeline:

```bash
python visualize_molecule.py
```

# Acknowledgements
[<u>Chembl UK</u>](https://www.ebi.ac.uk/chembl/) - Data source for compound information.

[<u>Selenium</u>](https://www.selenium.dev/) - Web scraping framework.

[<u>MageAI</u>](https://www.mage.ai/) - Microservices for data processing.

[<u>RDKit</u>](https://www.rdkit.org/) - Cheminformatics library for molecular visualizations.

[<u>PostgreSQL</u>](https://www.postgresql.org/) - Relational database management system.
