l1 = int(input("enter the first length of the triangle: "))
l2 = int(input("enter the second length of the triangle: "))
l3 = int(input("enter the third length of the triangle: "))
if l1 < 1 or l2 < 1 or l3 < 1:
    print("invalid lengths")
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print("valid triangle")
elif l1 == l2 == l3:
    print("equilateral triangle")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("isosceles triangle")
else:
    print("scalene triangle")  

if l1**2 + l2**2 == l3**2 or l1**2 + l3**2 == l2**2 or l2**2 + l3**2 == l1**2:
    print("right angled triangle")