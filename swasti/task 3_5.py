sentence = input("enter a sentence: ")
words = sentence.split()
number_of_words = len(words)
first_word = words [0]
last_word = words [-1]
python = False
if "python" in sentence.lower(): 
    python = True
else:
    python = False

for i in sentence.lower():
     if i == "e":
        sentence = sentence.replace("e", "3")

for j in sentence.lower():
     if j == "o":
        sentence = sentence.replace("o", "0")

print(number_of_words)
print(first_word)
print(last_word)
print("mentions python?:" , python)
print("leet version: ", sentence)