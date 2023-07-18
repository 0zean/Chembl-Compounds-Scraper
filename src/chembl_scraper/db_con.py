from os import getcwd

import yaml
from sqlalchemy import create_engine

credentials = getcwd()+"/credentials.yml"

with open(credentials, "r") as file:
    creds = yaml.safe_load(file)


def create_connection(password, database_name):
    
    # Credentials for authenticating into Postgres
    username = creds["username"]
    password = password
    host = creds["host"]
    port = creds["port"]
    db_name = creds["database"]
    
    # Create the dialect for Postgres
    dialect = f'postgresql://{username}:{password}@{host}:{port}/{db_name}'
    
    # Use the create_engine method
    engine = create_engine(dialect)
    
    return engine
