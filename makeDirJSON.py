import os
import json

# def path_to_dict(path):
#     a = [os.path.basename(path)]
#     d = {"parent": os.path.basename(path)}
#     x = {}
#     if os.path.isdir(path):
#         d["children"] = [
#             path_to_dict(os.path.join(path, x)) for x in os.listdir(path)
#         ]
#         x["children"] = ([
#             path_to_dict(os.path.join(path, x)) for x in os.listdir(path)
#         ])
#         a.append(x)
#     return d


def path_to_dict(path):
  root = {}
  if os.path.isfile(path):
    root = {"file": os.path.basename(path)}

  if os.path.isdir(path):
    root[os.path.basename(path)] = [
        path_to_dict(os.path.join(path, x)) for x in os.listdir(path)
    ]

    # print(os.path.join(path, x))
  return root


def createJSON(files, directories):
    with open("tree.json", "w") as outfile:
        json.dump(path_to_dict("."), outfile)


files = []
dirs = []
for root, directories, filenames in os.walk("."):
    files.append(filenames)
    dirs.append(directories)
createJSON(files, dirs)
