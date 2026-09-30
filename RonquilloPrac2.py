RonquilloStudents={"Ana":[98,85,82],
          "Liza":[72,73,78],
          "kirk":[68,71,84]
}

RonquilloLowest = 0
RonquillonameHighest = ""
RonquillonameLowest = 100
RonquilloHighest = ""
Ronquillotally = 0

for name, grade in Ronquillostudents.items();
average = sum(grade) / len(grade)
print(name, *grade, "Average:", average)
if average > RonquilloHighest:
    RonquilloHighest = average
    RonquillonameHighest = name
if average < RonquilloLowest:
    RonquilloLowest = average
    RonquillonameLowest = name
for g in grade:
    if g < 75:
        tally = Ronquillotally + 1

print(f"\nStudent {RonquillonameHighest} got the highest average: {RonquilloHighest}")
print(f"\nStudent {RonquillonameLowest} got the highest average: {RonquilloLowest}")
print(f"There are {Ronquillotally} grade which are below 75.")
