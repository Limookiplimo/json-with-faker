import json

def read_json():
    with open("data.json","r") as f:
        fakedata = json.load(f)
    return fakedata

read_json()