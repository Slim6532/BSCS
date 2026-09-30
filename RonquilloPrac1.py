RonquilloStudents = {
    "Ras": 85,
    "Riegn": 98,
    "Ziggy":78,
    "Ethan":95,
}
print("STUDENT GRADES")
print("--------------")
print("Ras:", RonquilloStudents["Ras"])
print("Riegn:", RonquilloStudents["Riegn"])

RonquilloStudents["Sam"] = 82
RonquilloStudents["Ziggy"] = 82
RonquilloStudents["Ethan"] = 91

RonquilloName1 = input("Enter Student Name: ")
RonquilloGrade1 = int(input("Enter Student Grade: "))

RonquilloStudents[RonquilloName1] = RonquilloGrade1
print(RonquilloStudents)
print("Update Student Grades")
print("\n-------------------")

for RonquilloName, RonquilloGrade in RonquilloStudents.items():
    print(RonquilloName, ":", RonquilloGrade)

RonquilloGrades = list(RonquilloStudents.values())
RonquilloLowest = min(RonquilloGrades)
RonquilloHighest = max(RonquilloGrades)
RonquilloDifference = RonquilloHighest - RonquilloLowest
RonquilloAverage = sum(RonquilloGrades) / len(RonquilloGrades)
RonquilloSort = sorted(RonquilloGrades)

print("Grade Statistics")
print("Lowest= ", RonquilloLowest)
print("Maximum:", RonquilloGrade)
print("Difference=", RonquilloDifference)
print("Average:", RonquilloAverage)
print("Sorted:", RonquilloSort)

search = input("\nEnter Student Name To Search: ")
if search in RonquilloStudents:
    print(search,"has a grade of",RonquilloStudents[search])
else:
    print("students not found")