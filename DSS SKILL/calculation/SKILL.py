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
    1. biggest-num
    2. caculator
    3. calendar
    4. even-odd
    ――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    """)

def execute_command(command):
    if command == '1':
        os.system('cmd /k "python calculation/DSS-bigest-num.py"' if os.name == 'nt' else 'python calculation/DSS-bigest-num.py')
    elif command == '2':
        os.system('cmd /k "python calculation/DSS-calculator.py"' if os.name == 'nt' else 'python calculation/DSS-calculator.py')
    elif command == '3':
        os.system('cmd /k "python calculation/DSS-calendar.py"' if os.name == 'nt' else 'python calculation/DSS-calendar.py')
    elif command == '4':
        os.system('cmd /k "python calculation/DSS-even-odd.py"' if os.name == 'nt' else 'python calculation/DSS-even-odd.py')

while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break

    execute_command(command)
