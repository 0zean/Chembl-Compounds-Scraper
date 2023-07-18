from getpass import getpass
from os import getcwd

import pandas as pd
from db_con import create_connection
from rdkit import Chem
from rdkit.Chem import Draw

# Connect to Postgres
pw = getpass("Type in your Postgres password here: ")
engine = create_connection(pw, "postgres")
cursor = engine.connect()

# Read the Feature Matrix Table as a Pandas DataFrame
df = pd.read_sql_table(table_name="compounds", con=cursor)

df['Name'] = df['Name'].astype(str)
df['Smiles'] = df['Smiles'].astype(str)

print(df.iloc[0]['Name'])

molecules_path = getcwd() + "/data/molecules/"


def smile_by_name(name):
    filter_df = df[df['Name'] == name]
    return filter_df.iloc[0]['Smiles']


# define the smiles string and covert it into a molecule sturcture
for name in df['Name']:
    if smile_by_name(name) != 'None':
        smile = str(smile_by_name(name))
        mol = Chem.MolFromSmiles(smile)
    
        fig = Draw.MolToFile(mol, molecules_path+name+'.png')

# draw the molecule with property
# for i, atom in enumerate(mol.GetAtoms()):
#     atom.SetProp("molAtomMapNumber", str(atom.GetIdx()))

# Draw.MolToFile(mol, molecules_path+'caffeine_with_prop.png')
