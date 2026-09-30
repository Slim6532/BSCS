#Ronquillo PROJECT
ronquillo = input("enter yor name: ").title()
print(f"Maayong Buntag, {ronquillo}!")

ronquillochoice = input("\n1.[power]\n2.[voltage]\n3.[current]\n\nOption:")

if ronquillochoice == "1":
    ronquillov = float(input("Enter Voltage: "))
    ronquilloc = float(input("Enter Current: "))
    ronquillop = ronquillov * ronquilloc
    print(f"Power: {ronquillop:.2f} P")

elif ronquillochoice == "2":
    ronquillop = float(input("Enter Power: "))
    ronquilloc = float(input("Enter Current: "))
    ronquillov = ronquillop / ronquilloc
    print(f"Voltage: {ronquillov:.2f} V")

elif ronquillochoice == "3":
    ronquillop = float(input("Enter Power: "))
    ronquillov = float(input("Enter Voltage: "))
    ronquilloc = ronquillop / ronquillov
    print(f"Current: {ronquilloc:.2f} A")

else:
    print("invalid option.")