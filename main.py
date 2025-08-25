import requests
import random

apiurl = "https://random-word-api.herokuapp.com/word?length=5"
response = requests.get(apiurl)
data = response.json() 
someword = random.choice(data)



def loop():

    
    while True:
        guess = input("Enter a word: " ) 
        let_check(guess)
        if len(guess) == len(someword):
            print(result)
        if guess  == someword:
            correct(guess)
            break
        
        
def count_check():
    count = 0
    while count != 6:
        loop()
        count += 1
    print("The word was: " + someword)

            
def let_check(guess):
    global result  
    result = ""
    for x in someword:
        wordLet = x
        for i in guess:
            newword = i
            if guess != someword and wordLet == newword:
                result += newword 
    if len(guess) < len(someword):
        print("Too Many Words Try Again")
    elif len(guess) > len(someword):
        print("Too Little Words Try Again")
    
            
                
def correct(guess):
    
    if guess == someword:
        print("Ding, Ding, Ding!!")
            

    
count_check()


                  
             
          









