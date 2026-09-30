print("UNIVERISTY OF MINAL")
grade = float(input("Enter Grade: "))
match grade:
    case 4.0:
        print("96-100")
    case 3.5:
        print("90-95")
    case 3.0:
        print("84-89")
    case 2.5:
        print("78-83")
    case 2.0:
        print("72-77")
    case 1.5:
        print("66-71")
    case 1.0:
        print("60-65")
    case _:
        print("Not in Range")