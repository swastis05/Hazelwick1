#caesar cipher#
message = input("Enter a message: ")
shift = int(input("Enter a shift value: "))
upper = message.upper()
final = []
for i in message: 
    shifted = ord(i) + shift
    final.append(chr(shifted))

print("encrypted message:", final)