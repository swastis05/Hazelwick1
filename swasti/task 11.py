#recursive subroutine 1
def countdown (n): 
    if n == 1: 
        return 1 
    else: 
        return n, countdown (n-1)


number = int(input("enter a number "))
answer = countdown(number)
print(answer)

#recursive subroutine 2

def reverse_string(s):
    if len(s)== 1: 
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

word = input("enter a word: ")
reverse = reverse_string(word)
print(reverse)

# recursive subroutine 3 

def is_palindrome(s):
    if len(s)== 1: 
        return True 
    elif s == reverse_string (s): 
        return True 
    else: 
        return False

palindrome = is_palindrome(word)
print(palindrome)

#recursive subroutine 4 

    