import json
import sys
from difflib import SequenceMatcher , get_close_matches

data = json.load(open("data.json"))

def similar(word):
    return get_close_matches(word,data.keys())

def meaning (word):


    try:

        defe = data[word]


        if type(defe) == list:

            length = len(defe)

            for i in range(length) :
                if i %2 == 0 :
                    print("\n \033[33m =",defe[i])
                else:
                    print("\n \033[35m =",defe[i])
    
        else:

            print(defe)
    
    
    except KeyError:

        print("\n\n\033[31m the word you entered does not exist in this dictonary sorry '‧º·(˚ ˃̣̣̥⌓˂̣̣̥ )‧º·'")
 
        return("\033[31m please try angain")        



print("this is a dictonary program")

word = input("enter the word :-  ")


flag = True

while flag != False:

    
    meaning(word.lower())


   
    print("\n \n \033[32m do you wish to find another word's defination \n(if no then type no \nand if yess just type the word and hit enter)")


    word =  input("\033[37m :-  ")

    if word == "no" or  word == "No":

        flag = False

print("Thank you for using the program \n good bye")