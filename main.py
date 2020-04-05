import json
import os
import sys
from difflib import SequenceMatcher , get_close_matches
from animation import *

data = json.load(open("data.json"))

no_of_words_defined = 0

def similar(word):
    matches =  get_close_matches(word,data.keys(),n = 3)
    lol = ""
    for i in matches:
        lol= lol+i+","
    return lol
    
    
    
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
        
        
        load_animation()
        
        
        print("did you mean one of these words\n\n \033[35m",similar(word))
        print("\n  \033[31m please try thease words or another one")        
        
        
        return(" ")


print("this is a dictonary program")

time.sleep(4)

word = input("enter the word :-  ")


flag = True

while flag != False:

    if os.name == "nt":os.system("cls")
    else:os.system("clear")
    
    print ("\033[32m for the word ",word)

    meaning(word.lower())


    if no_of_words_defined >3:
        print("\n \n \033[32m do you wish to find another word's defination \n(if no then type no \nand if yess just type the word and hit enter)")
    else:
        print("\n \n \033[32m  wanna go again, Just type the word.")

    word =  input("\033[37m :-")
  
      
      
        # for windows OS 
    if os.name =="nt": os.system("cls") 
          
    # for linux / Mac OS 
    else: os.system("clear") 



    if word == "no" or  word == "No":

        flag = False

print("Thank you for using the program \n good bye")