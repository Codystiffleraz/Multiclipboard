import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    # opening filepath, as varible f
    with open(filepath, "w") as f:
        # writes python dict as a json to the file
        json.dump(data, f)

def load_data(filepath):
    # try to load the file
    try:
        with open(filepath, "r") as f:
            # give python dict from json
            data = json.load(f)
            return data
    # if the file doesn't exist return any empty dictionary
    except:
        return {}
        
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    
    if command == "save":
        # asks for a key
        key = input("Enter a key: ")
        # store the value for the key as whatever is on clipboard
        data[key] = clipboard.paste()
        # rewrite the file and save the data
        save_data(SAVED_DATA,data)
        print("data saved")
    elif command == "load":
        key = input("Enter a key: ")
        # if the key is already in the dictionary
        if key in data:
            # access the value of the key in the dict & copy it to the clipboard
            clipboard.copy(data[key])
            print("data copied to clipboard.")
        else:
            print("Key does not exist")
    elif command == "list":
        print(data)
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command.")
    
