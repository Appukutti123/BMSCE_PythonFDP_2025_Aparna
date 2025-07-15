sub1 = int(input("enter the marks"))
sub2 = int(input("enter the marks"))
sub3 = int(input("enter the marks"))
sub4 = int(input("enter the marks"))
sub5 = int(input("enter the marks"))
if (sub1>=0) and (sub1<=100):
    if (sub2>=0) and (sub2<=100):
        if (sub3>=0) and (sub3<=100):
            if (sub4>=0) and (sub4<=100):
                if (sub5>=0) and (sub5<=100):
                    total = sub1 + sub2 + sub3 + sub4 + sub5
                    percentage = (total / 500) * 100
                    if percentage >= 75:
                        print(f"A")
                    elif(percentage>=50):
                        print(f"B")
                    elif(percentage>=30):
                        print(f"C")
                    else:
                        print(f"fail")
                else:
                    print(f"sub5 is INvalid")
            else:
                print(f"sub4 is INvalid")
        else:
            print(f"sub3 is INvalid")
    else:
         print(f"sub2 is INvalid")
else:
    print(f"sub1 is INvalid")