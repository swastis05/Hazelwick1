marks = 0
number = 0 
highest = 0 
lowest = 100
average = 0
total = 0

while marks != -1:
    marks = int(input("enter marks: "))
    if marks > 0 and marks < 100: 
        number = number + 1
        total = total + marks 
        if marks > highest: 
            highest = marks 
        if marks < lowest: 
            lowest = marks 
    else: 
        print("invalid")

average = total / number 
print("number of marks: ", number)
print("average mark: ", average)
print("highest mark is: ",highest)
print("lowest mark is: ", lowest)