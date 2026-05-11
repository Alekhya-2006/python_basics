# Reverse a string

def reverse_string(str):
    rev = ""
    for i in str:
        rev = i + rev
    return rev     

word = input("enter a word: ")
reverse = reverse_string(word)

print(f'The reverse of {word} is {reverse}')