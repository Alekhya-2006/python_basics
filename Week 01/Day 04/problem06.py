# palindrome funcction

def palindrome(word):
    p = ""

    for i in word:
        p  = i + p
    
    return "palindrome" if p == word  else "Not palindrome"  
      
Word = input("enter a word: ")
print(palindrome(Word)) 