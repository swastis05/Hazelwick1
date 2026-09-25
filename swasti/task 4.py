year = int(input("enter a year: "))
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0): 
    print("It is a leap year ")
    leap = True

month = int(input("enter a month number: "))
if month < 1 or month > 12:
    print("error")
if month == 2:
    if leap == True:
        print("29 days")
    else: 
        print("28 days")
elif month == 4 or month == 6 or month == 9 or month == 11: 
    print("30 days")
else: 
    print("31 days")