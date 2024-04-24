from random import *
import sys

words = ["laptop", "printer", "monitor", "keyboard", "mouse", "cpu", "ram", "graphic", "hard"]

print("_"*80,"\nHANGMAN\n")

n = randint(0,len(words)-1)
word = words[n]
charNumber = len(word)
guessLeft = len(word)  + 5
userList = ["-"]*charNumber
print(userList,"guess left:", guessLeft)

while userList.count("-") > 0 :
    guess = input("guess a character a-z: ")
    for i in range(charNumber) :
        if guess == word[i] :
            userList[i] = guess
    guessLeft -= 1
    print(userList,"guess left", guessLeft)
    print()
    if guessLeft < 1 :
        print("you lose!")
        sys.exit()
print("you won!")
