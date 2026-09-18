digit = int(input("Enter a 3 digit number: "))
hundreds = digit // 100 
tens1 = digit % 100
tens2 = tens1 // 10
units = tens2 % 10
sum = hundreds + tens2 + units 
reversed = str(units) + str(tens2) + str(hundreds)
if digit % 2 == 0: 
    print("Even number: True")
else: 
    print("Even number")
