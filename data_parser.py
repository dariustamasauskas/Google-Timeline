
# Import necessary packages
import json
import csv
import zipfile
import os

# Print the header of the parser to the screen
print('\nGoogle Timeline Data Parser')

# Define path and file names
path = 'E:/Career/Data Science/Projects/Google Timeline/Raw Data/'
file = 'Location History'

# Extract .json file from the zip archive
with zipfile.ZipFile(path + file + '.zip') as zf:
    zf.extractall(path)

# Load the extracted raw JSON file
with open(path + file + '.json') as LH:
    LocationHistory = json.load(LH)

# Extract distinct column names
columns = []
columns.append('counter')
for location in LocationHistory['locations']:
    for key in location.keys():
        if key not in columns:
            columns.append(key)

# Remove unnecessary columns
if 'activity' in columns:
    columns.remove('activity')
if 'verticalAccuracy' in columns:
    columns.remove('verticalAccuracy')

# Create .csv file for writing records
fn_path = './Parsed Data/'
fn = 'timeline_data.csv'
w = open(fn_path + fn, 'w', newline = '')
write = csv.writer(w)
write.writerow(columns)

# Print names of the columns to the screen
print('\nFile', fn, 'was created with', len(columns), 'columns')
for c in columns:
    print(c)

# Write records to .csv file for each column
counter = 0
for location in LocationHistory['locations']:
    counter += 1

    outcome_write = []
    outcome_write.append(counter)

    for col in columns[1:]:
        if col in location:
            outcome = location[col]
        else:
            outcome = None
        outcome_write.append(outcome)

    write.writerow(outcome_write)

# Print number of records appended to .csv file
print('\nFile', fn, 'was appended with', counter, 'records')

# Delete .json file and keep it only in zip archive
os.remove(path + file + '.json')
