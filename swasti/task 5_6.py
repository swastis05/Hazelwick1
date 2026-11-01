#prime finder
number = int(input("enter a number "))
prime = True
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            prime = False
if prime:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
