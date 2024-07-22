days=["SUNDAY","MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY"]
week = int(input("Enter the WEEK number(1-7): "))
index = week % 7
print("Days: ",days[index])
