import sys,os
from colorama import Fore

print(Fore.MAGENTA+"""

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
DSS SKILL
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

BY: darkstarshine2011
""")

def display_menu():
    print(Fore.YELLOW + """
    ―――――――――――――――――――――――――――――――――――――――――――――――――――――――
    1. dice
    2. guess number
    3. hangman
    ――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    """)

def execute_command(command):
    if command == '1':
        os.system('cmd /k "python games/DSS-dice.py"' if os.name == 'nt' else 'python games/DSS-dice.py')
    elif command == '2':
        os.system('cmd /k "python games/DSS-guess-number.py"' if os.name == 'nt' else 'python games/DSS-guess-number.py')
    elif command == '3':
        os.system('cmd /k "python games/DSS-hangman.py"' if os.name == 'nt' else 'python games/DSS-hangman.py')

while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break

    execute_command(command)
