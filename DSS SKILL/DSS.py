import sys,os
from colorama import Fore

print(Fore.MAGENTA+"""
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
DSS SKILL
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

BY: darkstarshine2011
""")

def display_menu():
    print(Fore.GREEN + """
    ----------------------------------------
    1: attack-tools
    2: calculation
    3: games
    ----------------------------------------
    """)

def execute_command(command):
    if command == '1':
        os.system('cmd /k "python attack-tools/SKILL.py"' if os.name == 'nt' else 'python attack-tools/SKILL.py')
    elif command == '2':
        os.system('cmd /k "python calculation/SKILL.py"' if os.name == 'nt' else 'python calculation/SKILL.py')
    elif command == '3':
        os.system('cmd /k "python games/SKILL.py"' if os.name == 'nt' else 'python info.py')

        display_menu()
    else:
        print('Invalid option! Please choose the correct one.')

while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break

    execute_command(command)
