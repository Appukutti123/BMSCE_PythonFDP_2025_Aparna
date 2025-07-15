def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

while True:
    num1 = int(input("Enter num1:"))
    num2 = int(input("Enter num2:"))

    Operation = int(input("Choose a operation:\n1)Addition\n2)subtraction\n3)Multiplication\n4)Divison\n5)Exit\n"))

    match Operation:
        case 1:
            print(f"your addition result is:", add(num1, num2))
        case 2:
             print(f"your subtraction result is:", sub(num1, num2))
        case 3:
            print(f"your multiplicaton result is:", mul(num1, num2))
        case 4:
             print(f"your divison result is:", div(num1, num2))
        case 5:
            print("okay byee")
        case _:
            print("invalid operation entered")
