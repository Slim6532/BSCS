Ronquillo_flavor = input("Enter your desired flavor (beef/pepperoni/hawaiian/cheese): ").lower()

if Ronquillo_flavor == "beef":
    print("You chose [ beef flavored pizza ]")
    print("\n")

elif Ronquillo_flavor == "pepperoni":
    print("You chose [ pepperoni pizza ]")
    print("\n")

elif Ronquillo_flavor == "hawaiian":
    print("You chose [ Hawaiian pizza ]")
    print("\n")

elif Ronquillo_flavor == "cheese":
    print("You chose [ cheese pizza ]")
    print("\n")

else:
    print("Invalid [ ]izza flavor ]")

    print("\n")
    exit()


Ronquillo_size = input("Enter size of your pizza (small/medium/large): ").lower()

match Ronquillo_size:
    case "small":
        Ronquillo_price = 180

    case "medium":
        Ronquillo_price = 250

    case "large":
        Ronquillo_price = 300

    case _:
        Ronquillo_price = 0
        print("Invalid size.")

if Ronquillo_price > 0:
    print("\n")
    print("Pizza price :"   , Ronquillo_price )
