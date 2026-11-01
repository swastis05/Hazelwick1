def count_char(text,ch):
    if len(text) == 0:
        return 0
    if text [0] == ch:
        return 1 + count_char(text[1:],ch)
    else:
        return count_char(text[1:],ch)

text = input("enter a string: ")
ch = input("enter a character: ")
count = count_char(text,ch)
print("the character", ch, "appears", count, "times in the string")