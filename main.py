


import random


words = ["pepsi","momo","pizza"]

letters = []
word = words[random.randit(len(words))]

print("Welcome to simple hangman")
life = 5
while life < 30 :
   guess = input("Enter the guessing word")
   if word.__contains__(guess):
       print("You have guessed right !!   ")
       letters.append(guess)
    if letters.__len__() == word.__len__():
           print("Congaratualtions you won")
           break
        else:
        lettersleft = word.__len__() - letters.__len__()
        print("You have" ,lettersleft,"left for game to be finished")
     else:
        life = life - 1
        if live == 0:
            print("Game over !! Better luck next time ")
            print("The word was", word)
            break
        else:
            ("You have ", live ,"left")

