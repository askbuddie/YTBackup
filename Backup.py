import os
import json

data = []

PATH_NAME = input('Enter Directory Name To Backup: ')

# creates the array
def create_file_lists(path):
    if os.path.isfile(path):
        data.append(os.path.relpath(path))

    if os.path.isdir(path):
        for x in os.listdir(path):
            # recursively get the files
            create_file_lists(os.path.join(path, x))
    return data


# create json file
def createJSON():
    with open(PATH_NAME + '.json', "w") as outfile:
        json.dump(create_file_lists(PATH_NAME), outfile)
        print('Successfully created ' + PATH_NAME + '.json')


createJSON()