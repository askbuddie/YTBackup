import os
import json
import json
import subprocess

def get_media_metadata(filename):
    result = subprocess.Popen(['hachoir-metadata', filename, '--raw'],
        stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    results = result.stdout.read().decode('utf-8').split('\r\n')

    # just a little bit of error checking
    if isinstance(results, list):
          try:
            if results[3].startswith('- height: '):
                return int(results[3].lstrip('- height: '))
            else:
              return None
          except IndexError:
            print('\n* No Dimensions Found for ' + filename)
            return None
    else:
      return None


data = []
PATH_NAME = input('Enter Directory Name To Backup: ')


# spinner strings
def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = spinning_cursor()


# creates the array
def create_file_lists(path):
    # spinner
    print("\rDoing Work ( {0} )".format(next(spinner)) , end="")


    if os.path.isfile(path):
        data.append([os.path.relpath(path), get_media_metadata(os.path.relpath(path))])
        
    if os.path.isdir(path):
        for x in os.listdir(path):
            # recursively get the files
            create_file_lists(os.path.join(path, x))
    return data


# create json file
def createJSON():
    with open(PATH_NAME + '.json', "w") as outfile:
        json.dump(create_file_lists(PATH_NAME), outfile)
        print('\nSuccessfully created ' + PATH_NAME + '.json')


createJSON()