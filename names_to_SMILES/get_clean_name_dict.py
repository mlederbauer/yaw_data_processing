import pandas as pd

# read in dictionary
name_dict = pd.read_csv('data_processing/yaw/name_dict.csv', sep=';', encoding='utf-8', header=0)
# set first column as name and second column as SMILES
name_dict.columns = ['Name', 'SMILES']
count = 0

# 4936 showed ;None as an entry - it was deleted manually

# for each name in dictionary, check if SMILES is None
# if so, delete name from dictionary
for name in name_dict['Name']:
    if name_dict[name_dict['Name'] == name]['SMILES'].values[0] == 'None':
        name_dict = name_dict[name_dict['Name'] != name]
        count += 1
        print('Deleted name: {}'.format(name))

# save dictionary as .csv file
print('Number of names deleted: {}'.format(count))
name_dict.to_csv('data_processing/yaw/name_dict_clean.csv', sep=';', encoding='utf-8')