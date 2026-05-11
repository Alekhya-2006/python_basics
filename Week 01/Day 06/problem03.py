# count  vowels

def count(n):

    vowels = 0

    for i in n:

        if (i == "a" or i == "e" or
            i == "i" or i == "o" or
            i == "u"):

            vowels += 1
    return vowels        

word = input("enter a word: ")

print(f'The number of vowels in {word} is {count(word)}')