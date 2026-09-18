name = input("what is your name?: ")
height = float(input("enter your height in cm: "))
height_metres = (height/100)
INCH = 2.54
height_inches = (height/ INCH)
print("Hi" + name)
print("Your height is" + str(height_metres))
print("That is" + str(height_inches))
if height > 180: 
    print("Taller than 180cm: True")
else: 
    print("Taller than 180cm: False")