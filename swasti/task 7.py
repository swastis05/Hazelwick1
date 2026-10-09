rows = 5
seats = 8 

plan = []
for i in range (rows): 
    plan.append(["0"] * seats)

for row in range (len(plan)): 
    print(row + 1)
    for col in range (len(plan[row])):
        print(col + 1)
        print(plan[row][col], end = "\t")
    print()

q_row = int(input("what row do you want to book?: "))
q_seat = int(input("what seat do you want to book?: "))

if plan [q_row] [q_seat] == "0": 
    [q_row, q_seat] == "X"
    print("booked")
else: 
    print("this seat is already booked")

for row in range (len(plan)): 
    for col in range (len(plan[row])): 
        if [row, col] == "0": 
            free = free + 1 

print("number of free seats: ", free)
