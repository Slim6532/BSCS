#RonquilloW9A2
#TAYVON-KEY-KYC-EYX
#PYTHON-LONG-LONG
str(input("\nInput name:"))
print(f"\nM E L J A Y - L O A D E D\n ")
RonquilloItems = int(input("Enter Item:"))
RonquilloScore = int(input("Enter Score:"))

print("\nScore Percentage            Color")
print("90 - 96                    [light green]")
print("80 - 89                    [yellow green]")
print("70 - 79                    [yellow]")
print("60 - 69                    [orange]")
print("59 - below                    [red]")

RonquilloRatio = RonquilloScore/RonquilloItems * 100

if RonquilloRatio >= 90 and RonquilloRatio >= 96:
    print(f"\n-Light green\n-Score Percentage: {RonquilloRatio:}%\n-Passed")
elif RonquilloRatio >= 80 and RonquilloRatio >= 89:
    print(f"\n-Yellow green\n-Score Percentage: {RonquilloRatio:}%\n-Passed")
elif RonquilloRatio >= 70 and RonquilloRatio >= 79:
    print(f"\n-Yellow\n-Score Percentage: {RonquilloRatio:}%\n-Passed")
elif RonquilloRatio >= 60 and RonquilloRatio >= 69:
    print(f"\n-Orange\n-Score Percentage: {RonquilloRatio:}%\n-Passed")
elif RonquilloRatio >= 59 and RonquilloRatio >= 50:
    print(f"\n-Red\n-Score Percentage: {RonquilloRatio:}%\n-Failed")
else:
    print("Invalid Input")

