import json

def load(file, useKeysAsIndex=False):
    with open(file) as data_file:
        return json.load(data_file)

def parseKeysAsIndex(data):
    new = {}
    for i in data:
        new[int(i)] = data[i]

    return new
