Ronquillostudents = [("Jonah Perez", "BSCS","bscs",1),
            ("Alex Santos", "BSMT",2),
            ("Micah Mendoza", "BSCS",1),
            ("Allen Torres", "BSMT",2),
            ("Zach Rajid", "BSCS",3),
            ("Ziggy Echaveria", "BSMT",4),
            ("Tristan Mongcal", "BSCS",3),
            ("Jayden Farraz", "BSMT",4),
            ("Ras Garcia", "BSMT",3),
            ("Daniel Morales", "BSCS",4)]

print("  ---STUDENT INFORMATION---")
print("---ENTER IN A CAPITAL LETTER---\n")
Ronquilloprogram = input("Enter Program: ")
Ronquilloyear = int(input("Enter Year Level: "))
Ronquillofound = False

for Ronquillostudents in Ronquillostudents:
    if Ronquillostudents[1] == Ronquilloprogram and Ronquillostudents[2] == Ronquilloyear:
       print("\nName: ", Ronquillostudents[0])
       print("Program: ", Ronquillostudents[1])
       print("Year Level: ", Ronquillostudents[2])
       Ronquillofound = True

if Ronquillofound:
    print("STUDENT FOUND")
else:
    print("COULDN'T FETCH STUDENT INFORMATION!")
