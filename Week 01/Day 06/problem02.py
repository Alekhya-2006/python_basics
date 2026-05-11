# count chars without using len()

def count(n):

    chars = 0
    
    for i in n:
        chars += 1

    return chars

word = input("enter a word: ")    

print(f'Number of characters in {word} is {count(word)}')