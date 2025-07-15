balance = int(input("enter the balance amount"))
withdraw = int(input("enter amount to be withdraw"))
if withdraw<=balance:
    print(f"transaction successful")
else:
    print (f"insufficient balance")
