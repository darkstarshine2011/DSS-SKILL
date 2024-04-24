print("_"*80, "\nCALCULATOR\n")

def cal(N1,ac,N2) :
    if ac == "*" :
        print("\n\n\nanswer is\n")
        print("-"*80)
        print(N1 * N2)
        print("-"*80)
    if ac == "/" :
        print("\n\n\nanswer is\n")
        print("-"*80)
        print(N1 / N2)
        print("-"*80)
    if ac == "+" :
        print("\n\n\nanswer is\n")
        print("-"*80)
        print(N1 + N2)
        print("-"*80)
    if ac == "-" :
        print("\n\n\nanswer is\n")
        print("-"*80)
        print(N1 - N2)
        print("-"*80)
    if ac == "**" :
        print("\n\n\nanswer is\n")
        print("-"*80)
        print(N1 ** N2)
        print("-"*80)
    if ac == "//" :
        print("\n\n\nanswer is\n")
        print("-"*80)
        print(N1 // N2)
        print("-"*80)
    if ac == "%" :
        print("\n\n\nanswer is\n")
        print("-"*80)
        print(N1 % N2)
        print("-"*80)

number1 = float(input("put the first number\n"))
action = str(input("select action\n"))
number2 = float(input("put the next number\n"))

cal(number1,action,number2)
