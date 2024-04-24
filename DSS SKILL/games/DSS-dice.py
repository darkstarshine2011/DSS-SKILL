from random import *
import sys
print("_"*80, "\nDICE\n")

turn = ""

def DICE() :
    dice = randint(1,6)
    print("-"*80)
    print(dice)
    print("-"*80)

while True :
    turn = input("\n\njust press ENTER to roll the dice\n")
    if turn == "":
        DICE()
    else:
        sys.exit()
