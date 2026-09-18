digit = int(input("Enter a 3 digit number: "))
hundreds = digit // 100 
tens1 = digit % 100
tens2 = tens1 // 10
units = tens1 % 10
sum = hundreds + tens2 + units 
reversed = str(units) + str(tens2) + str(hundreds)
print("Hundreds: " , hundreds)
print("Tens: ", tens2)
print("Units: ", units)
print("Sum of digits: ", sum)
print("Reversed: " + reversed)
if digit % 2 == 0: 
    print("Even number: True")
else: 
    print("Even number: False")
