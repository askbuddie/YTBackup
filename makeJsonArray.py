import os
import json

data = []


def path_to_dict(path):

    if os.path.isfile(path):
        data.append(os.path.relpath(path))

    if os.path.isdir(path):
        for x in os.listdir(path):
            path_to_dict(os.path.join(path, x))
    print(data)
    return data


# create json file
def createJSON():
    with open("tree.json", "w") as outfile:
        json.dump(path_to_dict("./videos"), outfile)


createJSON()