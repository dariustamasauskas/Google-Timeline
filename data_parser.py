
# Import necessary packages
import json
import csv
import zipfile
import os

def data_parser():

    # Print the header of the parser to the screen
    print('\nGoogle Timeline Data Parser\nWorking...')

    # Define path and file names
    path = './data/raw/'
    file = 'Location History'

    # Extract .json file from the zip archive
    with zipfile.ZipFile(path + file + '.zip') as zf:
        zf.extractall(path)

    # Load the extracted raw JSON file
    with open(path + file + '.json') as lh:
        location_history = json.load(lh)

    # Extract distinct column names
    columns = []
    columns.append('id')
    for location in location_history['locations']:
        for key in location.keys():
            if key not in columns:
                columns.append(key)

    # Remove unnecessary columns
    remove_cols = ['activity','verticalAccuracy','velocity','heading','altitude']
    for col in remove_cols:
        if col in columns:
            columns.remove(col)

    # Create .csv file for writing records
    fn_path = './data/parsed/'
    fn = 'timeline_data.csv'
    w = open(fn_path + fn, 'w', newline = '')
    write = csv.writer(w)
    write.writerow(columns)

    # Print names of the columns to the screen
    print('\nFile', fn, 'was created with', len(columns), 'columns:')
    for c in columns:
        print(c)

    # Write records to .csv file for each column
    id = 0
    for location in location_history['locations']:
        id += 1

        outcome_write = []
        outcome_write.append(id)

        for col in columns[1:]:
            if col in location:
                outcome = location[col]
            else:
                outcome = None
            outcome_write.append(outcome)

        write.writerow(outcome_write)

    # Print number of records appended to .csv file
    print('\nFile', fn, 'was appended with', id, 'records.')

    # Delete .json file and keep it only in zip archive
    os.remove(path + file + '.json')

if __name__ == "__main__":
    data_parser()
