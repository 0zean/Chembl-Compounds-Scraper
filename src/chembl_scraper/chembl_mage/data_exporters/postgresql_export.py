from os import getcwd

import yaml
from sqlalchemy import create_engine

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

# PostgreSQL credentials
credentials = getcwd()+"/credentials.yml"

with open(credentials, "r") as file:
    creds = yaml.safe_load(file)


# Helper Function 1: Create connection Object
def create_con_object():
    user = creds["username"]
    password = creds['password']
    host = creds["host"]
    port = creds["port"]
    db_name = creds["database"]

    # Postgres JDBC Protocol
    dialect = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'

    # DB Engine
    engine = create_engine(dialect)

    # Cursor variable: Connection Object
    return engine.connect()


@data_exporter
def export_data(data, *args, **kwargs):
    """
    Exports data to some source.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    # Specify your data exporting logic here
    cursor = create_con_object()

    data.to_sql('compounds', con=cursor, index=False, if_exists='replace')
