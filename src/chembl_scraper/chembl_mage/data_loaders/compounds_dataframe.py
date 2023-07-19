import os
import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your data loading logic here
    path = os.getcwd()
    df_folder = path + '/data/chembl_compounds/dataframe'
    compounds_folder = path + '/data/chembl_compounds/compounds'
    output_file = df_folder + '/combined_data.csv'

    # check if dataframe exists yet
    if os.path.exists(df_folder) and os.listdir(df_folder):
        existing_df = pd.read_csv(output_file)

        # Get a list of CSV files in compounds folder
        csv_files = [f for f in os.listdir(compounds_folder) if f.endswith('.csv')]

        # Append CSV files to the existing DataFrame, delete CSVs
        dfs = [existing_df]
        for csv_file in csv_files:
            file_path = os.path.join(compounds_folder, csv_file)
            df = pd.read_csv(file_path, sep=";")
            dfs.append(df)
            os.remove(file_path)
        combined_df = pd.concat(dfs)

    else:
        # Get a list of CSV files in compounds folder
        csv_files = [f for f in os.listdir(compounds_folder) if f.endswith('.csv')]

        # Combine CSV files into a single DataFrame, delete CSVs
        dfs = []
        for csv_file in csv_files:
            file_path = os.path.join(compounds_folder, csv_file)
            df = pd.read_csv(file_path, sep=";")
            dfs.append(df)
            os.remove(file_path)
        combined_df = pd.concat(dfs)

        # Make df folder in case it doesn't exist yet
        os.makedirs(df_folder, exist_ok=True)

    # Remove rows with no compound name
    combined_df.dropna(subset=["Name"], inplace=True)

    # Save the updated combined DataFrame to df folder
    combined_df.to_csv(output_file, index=False)

    return combined_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
