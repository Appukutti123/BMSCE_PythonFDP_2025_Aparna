#Infinite while loop, we will create a menu and the user will choose from that menu until the loop runs
#menu would look like
#1say hello
#2say bye
#3exit
#use while true:
while True:
    print("1. Say Hello\n 2. Say Bye\n 3. Exit")
    choice = int(input('Enter a Choice'))
    if choice==1:
        print("Hello")
    elif choice==2:
        print("Bye")
    elif choice==3:
        print("ok exiting..")
        break
else:
    print("invalid choice")


