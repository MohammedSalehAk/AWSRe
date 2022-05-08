import json

def readJsonFile(insulin):
    data = ""
    try:
        with open(insulin) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data 
