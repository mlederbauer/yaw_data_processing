# Script to get SMILES strings from IUPAC names in Yaw Handbook
# Use Map to get to molecules more quickly

import pandas as pd
import numpy as np
from rdkit import Chem
from urllib.request import urlopen
from urllib.parse import quote
import os


def SMILES_from_IUPAC(ids):
    try:
        url = 'http://cactus.nci.nih.gov/chemical/structure/' + quote(ids) + '/smiles'
        ans = urlopen(url).read().decode('utf8')
        ans = Chem.MolToSmiles(Chem.MolFromSmiles(ans))
        return ans
    except:
        return 'None'


# get the Name and add it to a dictionary called name_dict
# the key is the Name, the value is SMILES_from_IUPAC(key)
name_dict = {}

# loop over all .csv files in folder ./data
file_list = os.listdir('data_processing/yaw/raw_data/')
for file in file_list:
    if file.startswith('data') and file.endswith('.csv'):
        print(file)
        # read in file
        df = pd.read_csv('data_processing/yaw/raw_data/{}'.format(file),sep=";",encoding="utf-8",index_col=0,header=0)
        # select name column
        for name in df.iloc[:, 0]:
            # check if name is already in dictionary
            if name not in name_dict:
                name_dict[name] = SMILES_from_IUPAC(name)
                print(name, name_dict[name])
            if len(name_dict) % 100 == 0:
                print(len(name_dict))

# print first 10 items in dictionary
print(list(name_dict.items())[:10])

# save dictionary as .csv file
df = pd.DataFrame.from_dict(name_dict, orient='index')
df.to_csv('data_processing/yaw/name_dict.csv', sep=';', encoding='utf-8')