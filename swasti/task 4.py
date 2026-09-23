year = int(input("enter a year: "))
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0): 
    print("It is a leap year ")
    leap = True

month = int(input("enter a month number: "))
if month < 1 or month > 12:
    print("error")
if month == "Februrary"
