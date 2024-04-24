print("_"*80, "\nBIGEST NUMBER\n")

def bigger(num1,num2,num3,num4,num5):
    if num1 > num2 :
        b1 = num1
    else:
        b1 = num2
    if b1 > num3 :
        b2 = b1
    else:
        b2 = num3
    if b2 > num4 :
        b3 = b2
    else:
        b3 = num4
    if b3 > num5 :
        b4 = b3
    else:
        b4 = num5

    print("\n\nthe bigger one is:")
    print(b4)

N1 = float(input("number1\n"))
N2 = float(input("number2\n"))
N3 = float(input("number3\n"))
N4 = float(input("number4\n"))
N5 = float(input("number5\n"))

bigger(N1,N2,N3,N4,N5)
