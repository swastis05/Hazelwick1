pence = int(input("Enter the amount in pence: "))
two_pounds = pence // 200
two_remaining = pence % 200
one_pound = two_remaining // 100
one_remaining = two_remaining % 100
fifty_pence = one_remaining // 50
fifty_remaining = one_remaining % 50
twenty_pence = fifty_remaining // 20
twenty_remaining = fifty_remaining % 20
ten_pence = twenty_remaining // 10
ten_remaining = twenty_remaining % 10
five_pence = ten_remaining // 5
five_remaining = ten_remaining % 5
two_pence = five_remaining // 2 
two_remaining = five_remaining % 2
one_pence = two_remaining // 1
print("£2 coins: ", two_pounds)
print("£1 coins: ", one_pound)
print("50p coins: ", fifty_pence)
print("20p coins: ", twenty_pence)
print("10p coins: ", ten_pence)
print("5p coins: ", five_pence)
print("2p coins: ", two_pence)
print("1p coins: ", one_pence)