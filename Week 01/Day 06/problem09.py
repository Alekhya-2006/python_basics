# replace vowels

def replace(n):
    s = ""

    for i in n:

        if i in "aeiou":
            i = '*'
        
        s += i    

    return s    

word = input("enter a word: ")
print(replace(word))