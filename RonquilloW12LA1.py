salary = {"E104":{
"EmpName": "Meljay Ronquillo",
"DailyHrs": [8,9,8.5,10,8]
},
"E601":{
"Employee Name":"Nikka Salary",
"DailyHrs": [9,10,8,8,9]
}
}
emp_id = input("Enter Employee ID: ")
if emp_id not in salary:
    print("Not Found")
else:
    employee = salary[emp_id]
    emp_name = employee["EmpName"]
    daily_hrs = employee["DailyHrs"]

    print(f"Name: {emp_name}")
    print(f"DutyHours: {daily_hrs}")

    weeklybasic = 9000
    rateperhour = weeklybasic / 40

    total_week_hours = sum(daily_hrs)

    overtime = 0
    for hrs in daily_hrs:
        if hrs > - 8:
            excess = hrs - 8
            overtime += excess * (1.5 * rateperhour)

    GrossPay = (40 * rateperhour) + overtime

print(f"Total week hours: {total_week_hours}")
print(f"Overtime: {overtime:2f}")
print(f"Gross pay: {GrossPay:.2f}")