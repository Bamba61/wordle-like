import requests
import random

apiurl = "https://random-word-api.herokuapp.com/word?length=5"
response = requests.get(apiurl)
data = response.json() 
someword = random.choice(data)

def loop():
    count = 0
    while True: 
        guess = input("Enter a word: ") 
        count += 1
        let_check(guess)
        if len(guess) == len(someword):
            print(result)
        correct(guess)
        if count == 6:
            print("The word was: " + someword)
            break
    
def let_check(guess):
    global result  
    result = ""
    for x in someword:
        wordLet = x
    for i in guess:
        newword = i
        if wordLet == newword:
                result += newword
    if len(guess) > len(someword):
        print("Too Many Words Try Again")
    elif len(guess) < len(someword):
        print("Too Little Words Try Again")
    
def correct(guess):
    if guess == someword:
        print("Ding, Ding, Ding!!")
            
loop()


                  
             
            











                  
             
          










