
import pandas as pd
from datetime import date

list_files_json = ['sf.json', 'xsoar.json']
#corvert jso to csv
for file in list_files_json:
    # read json file
    files_in_json = pd.read_json(file)
    # convert files to csv and replace de json to cvs for extention
    files_in_csv = files_in_json.to_csv(file.replace('json', 'csv'), sep=',', index=False)

print('json to csv done :)')

