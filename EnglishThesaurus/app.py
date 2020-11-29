import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input(f"Did you mean {get_close_matches(word, data.keys())[0]} instead? y/n: ")
        if yn.lower() == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn.lower() == "n":
            return "Word doesn't exist. Please double check it"
        else:
            return "Not a valid input."
    else:
        return "The word doesn't exist" 

word = input("Enter word: ")
output = translate(word)

if isinstance(output, list):
    for item in output:
        print(item)
else:
    print(output)