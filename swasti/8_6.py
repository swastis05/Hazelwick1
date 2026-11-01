def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for i in text.lower():
        if i in vowels: 
            count = count + 1 
    return count

def longest_word(text):
    words = text.split()
    longest = 0 
    for i in words: 
        if len (i) > longest: 
            longest = i
    return longest

def capitalise_words(text):
    words = text.split()
    for i in words: 
        i[0] = i[0].upper()
    return " ".join(words)

def is_pangram(text):
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in letters: 
        if i not in text.lower():
            return False
    return True

text = input("enter a sentence: ")
vowels = count_vowels(text)
longest = longest_word(text)
capitalised = capitalise_words(text)
pangram = is_pangram(text)  
print("Number of vowels:", vowels)
print("Longest word:", longest)
print("Capitalised sentence:", capitalised)
if pangram:
    print("The sentence is a pangram.") 
    