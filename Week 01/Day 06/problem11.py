# remove duplicates

def remove_duplicates(n):
    s = ""
    
    for i in n:
       if i not in s:
           s += i

    return s

word = input("enter a word: ")

print(remove_duplicates(word))