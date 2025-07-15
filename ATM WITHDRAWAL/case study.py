fruit = input("Enter a fruit :")
match fruit:
    case "apple":
        print(f"you have given a apple")
    case "mango":
        print(f"you have given a mango")
    case "orange":
        print(f"you have given a orange")
    case _:
        print(f"maybe some random fruit or invalid entry")