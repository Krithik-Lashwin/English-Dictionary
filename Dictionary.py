import json
from difflib import get_close_matches
data = json.load(open('dictionary.json'))
def translate(word):
    word = word.lower()
    if(word in data):
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        y = input('Do you mean %s instead of this? Enter y if yes or n if no' %get_close_matches(word,data.keys())[0])
        y = y.lower()
        if y == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif y == 'n':
            return 'This word does not seem to exist. Please check for any spelling mistakes or errors in this word to get better results'
        else:
            return 'We did not understand your word, Please check if this word exists'
    else:
        return 'This word does not seem to exist. Please check for any spelling mistakes or errors in this word to get better results'
word = input('Enter a word: ')
output = translate(word)
if(type(output) == list):
    for item in output:
        print(item)
else:
    print(output)