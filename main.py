import json


data = json.load(open("data.json"))

def meaning (word):
    try:
        return data[word]
    except KeyError:
        print("the word you entered does not exist in this dictonary sorry ಥ_ಥ")
        return("please try anain")        

word = input("enter the word :-  ")


flag = True

while flag != False:

    try:
        print(meaning(word))
    except print(""):
        pass


   
    print("\n \n do you wish to find another word's defination \n(if no then type no \nand if yess just type the word and hit enter)")


    word =  input(":-  ")

    if word == "no" or  word == "No":
        flag = False

print("Thank you for using the program \n good bye")