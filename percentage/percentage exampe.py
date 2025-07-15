sub1 = int(input("enter the marks"))
sub2 = int(input("enter the marks"))
sub3 = int(input("enter the marks"))
sub4 = int(input("enter the marks"))
sub5 = int(input("enter the marks"))
total= sub1+sub2+sub3+sub4+sub5
percentage = (total/500) * 100
if percentage>=75:
    print(f"A")
elif percentage>=50:
    print(f"B")
elif percentage >= 30:
    print(f"C")
else:
    print(f"fail")
