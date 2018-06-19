#This script will create a JSON file defining a slot type from a given list of types in the following format
#line 1: Slot Name
#line 2: Slot Description
#line 3: Value Selection Strategy [ORIGINAL_VALUE] or [TOP_RESOLUTION]
#line 4 onwards: Slot Name
#
#NOTE synonyms are not added by default but can be added later within LEX

import zipfile
import argparse
import json

parser = argparse.ArgumentParser(description='Create Slot Type JSON file to import to LEX')
parser.add_argument('list', metavar='l', type=str, nargs='+',
                   help='The list to be converted. Open this file in a text editor to see the list syntax')
parser.add_argument('output', metavar='o', type=str, nargs='+',
                   help='the name of the destination file')

args = parser.parse_args()

#open the list and save as python variable
with open(args.list[0], 'r') as inFile:
    input = inFile.read()
    inFile.close()
#split list on new lines to create array
values = input.split('\n')
#check for empty lines
for value in values:
    if value == "":
        values.remove(value)


print(values)

slotName = values[0]
slotDesc = values[1]
valueSelectionStrategy = values[2]


enumerationValues = ''
for value in values[3:]:
    if enumerationValues != '':
        enumerationValues += ','
    enumerationValues += '{"value": "'+value+'"}'


#create JSON string
output = '{"metadata": {"schemaVersion": "1.0","importType": "LEX","importFormat": "JSON"},"resource": {"name": "'+slotName+'","description": "'+slotDesc+'","version": "version number","enumerationValues": ['+enumerationValues+'],"valueSelectionStrategy": "'+valueSelectionStrategy+'"}}'

#JSON string to python object then prettify it using JSON library

decoder = json.JSONDecoder()
output = decoder.decode(output)
prettyOut = json.dumps(output, sort_keys=True, indent=4)



with open(args.output[0]+'.JSON','w') as fileToWrite:
    fileToWrite.write(prettyOut)
    fileToWrite.close()
    with zipfile.ZipFile(str(args.output[0]+'.zip'),'w') as zip:
        zip.write(str(fileToWrite.name))
        zip.close()




