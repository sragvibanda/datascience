"""
1. Write a function count_vowels(word)that takes a word as an 
argument and returns the number of vowels in the word

"""

def count_vowels(word):
    vowel_counter = 0
    for char in word:
        if char == "a" or char == "A":
            vowel_counter += 1
        elif char == "e" or char == "E":
            vowel_counter += 1
        elif char == "i" or char == "I": 
            vowel_counter += 1
        elif char == "o" or char == "O":
            vowel_counter += 1
        elif char == "u" or char == "U":
            vowel_counter += 1
    
    return vowel_counter

def main():
    vowel_counter = count_vowels("WATERBOTTLE")
    print("The number of vowels:", vowel_counter)

main()








