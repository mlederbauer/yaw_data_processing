# yaw-data-processing
Data Processing Scripts for Yaw's Handbook of Thermodynamic and Physical Properties of Chemical Compounds

1. names_to_SMILES
- get_SMILES_from_IUPAC.py
- get_clean_name_dict.py
- name_dict.csv
- name_dict_clean.csv: clean version of name_dict.csv without None, used for further data processing (10145 unique SMILES/molecules)

2. data_preparation
- clean_raw_data.ipynb: clean raw data from Yaws' Handbook, from raw .csv file from a parsed excel file (single_data_names) to .csv file with all SMILES, parameters and temperature ranges (single_data_SMILES)


3. data