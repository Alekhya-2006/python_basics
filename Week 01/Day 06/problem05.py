# check whether a string is palindrome:

def check(str):

    rev = ""

    for i in str:
        rev = i + rev

    return "Palindrome" if rev == str else "Not palindrome"

word = input("enter a word: ")

print(check(word))