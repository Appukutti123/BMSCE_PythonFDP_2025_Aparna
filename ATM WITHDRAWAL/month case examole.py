month = input("Enter a month:")
match month:
    case "1":
        print(f"Jan")
    case "2":
        print(f"FEB")
    case "3":
        print(f"MAR")
    case "4":
        print(f"APR")
    case "5":
        print(f"MAY")
    case "6":
        print(f"JUN")
    case "7":
        print(f"JUL")
    case "8":
        print(f"AUG")
    case "9":
        print(f"SEP")
    case "10":
        print(f"OCT")
    case "11":
        print(f"NOV")
    case "12":
        print(f"DEC")
    case _:
        print(f"invalid MONTH")