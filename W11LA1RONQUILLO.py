while True:

    Ronquillo_flavor = input(
        "Enter your desired flavor (beef/pepperoni/hawaiian/cheese): ").lower()

    if Ronquillo_flavor == "beef":
        print("You chose [ beef flavored pizza ]")

    elif Ronquillo_flavor == "pepperoni":
        print("You chose [ pepperoni pizza ]")

    elif Ronquillo_flavor == "hawaiian":
        print("You chose [ Hawaiian pizza ]")

    elif Ronquillo_flavor == "cheese":
        print("You chose [ cheese pizza ]")

    else:
        print("Invalid pizza flavor.")
        print()
        continue

    print()

    Ronquillo_size = input(
        "Enter size of your pizza (small/medium/large): ").lower()

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
        print()
        print("Pizza price:", Ronquillo_price)

    again = input("Do you want to enter again? Y/N: ")

    if again.upper() != "Y":
        print("Program ended.")
        break