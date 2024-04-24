from random import seed
from random import randint

num = randint(0,1000000)
guess_count = 0
player_guess = ""

print("_"*80, "\nGUESS NUMBER\n")

def guess(number,GuessCount,guessed):
    guessed = int(input("guess the number(0 to 1000000)  "))
    GuessCount = GuessCount + 1
    if guessed < number:
        print("the number is bigger than your guess\n")
    if guessed > number:
        print("the number is smaller than your guess\n")
    if guessed == number:
        print("congratulations! You guessed the number right! Number of your guesses:")
        print(GuessCount)
        print("\n\n\n\n\nlet's play a new raund")

while num != player_guess:
    guess(num,guess_count,player_guess)
