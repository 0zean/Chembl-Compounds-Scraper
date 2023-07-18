import os
from zipfile import ZipFile

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
    path = os.getcwd() + "/data/chembl_compounds/"
    status = None

    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)) and file.endswith('.zip'):
            # unzip
            with ZipFile(path+file, "r") as zObject:
                # list all files in zip file
                csv = zObject.namelist()
                zObject.extract(csv[0], path=path+"/compounds")
            
            # close extraction
            zObject.close()

            # rename csv to compound name
            os.rename(os.path.join(path+"/compounds/", csv[0]), 
                  os.path.join(path+"/compounds/", os.path.splitext(file)[0]+'.csv'))

            # remove .zip file after extraction
            os.remove(os.path.join(path, file))
            status = "Successfully unziped file(s)"

        else:
            status = "No file(s) to unzip"

    return status


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
