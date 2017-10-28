import json
import keyword
from difflib import get_close_matches
d=json.load(open("data.json"))#load json data to Python Dictionary
keyslist=d.keys() #create a list of keys
def synonym (x):
    #x = x.replace(' ', '')#remove space
    #x=x.lower() #Make it case INsensitive
    if x in d:
        return (','.join(d[x]))

    elif x.lower() in d:                    #condition for proper nouns like Delhi/Paris whose first letters are upper case in the data
        return(','.join(d[x.lower()]))
        #condition for mispelling
        #first check for matches

    elif len (get_close_matches(x, keyslist, 3)) > 0:   #if there are matches (length of list>0)
        #ask user to unput Y or N to continue by choosing first element of list of close matches
        yn=input("Did you mean %s instead ? Enter Y if Yes and N if No: " % get_close_matches(x, keyslist, 3)[0])
        if (yn=='Y') or (yn=='y'): #condition to check if user entered Y or No
            #return the word plus its definition
            return (str(get_close_matches(x, keyslist, 3)[0])+": "+','.join(d[get_close_matches(x, keyslist, 3)[0]]))
        else:
            return ("Word Doesn't exist")

    else:
        return ("Word doesn't exist")



word=input("Enter the word: ")
output=synonym(word)#call the function
print(output)
