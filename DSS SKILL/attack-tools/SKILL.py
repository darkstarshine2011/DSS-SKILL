import sys,os
from colorama import Fore

print(Fore.MAGENTA+"""

――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
DSS SKILL
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

BY: darkstarshone2011
""")

def display_menu():
    print(Fore.YELLOW + """
    ―――――――――――――――――――――――――――――――――――――――――――――――――――――――
    1. fake-user
    2. IP-finder
    3. port-scanner
    ――――――――――――――――――――――――――――――――――――――――――――――――――――――――
    """)

def execute_command(command):
    if command == '1':
        os.system('cmd /k "python attack-tools/DSS-fake-user.py"' if os.name == 'nt' else 'python attack-tools/DSS-fake-user.py')
    elif command == '2':
        os.system('cmd /k "python attack-tools/DSS-IP-finder.py"' if os.name == 'nt' else 'python attack-tools/DSS-IP-finder.py')
    elif command == '3':
        os.system('cmd /k "python attack-tools/DSS-port-scanner.py"' if os.name == 'nt' else 'python attack-tools/DSS-port-scanner.py')

while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break

    execute_command(command)
