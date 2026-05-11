# count uppercase and lower case letters

def case(n):

    up_count = 0
    low_count = 0

    for i in n:

        if i >= "A" and i <= "Z":
            up_count += 1
        
        elif i >= "a" and i <= "z":
            low_count += 1
        
    print("uppercase: ",up_count)
    print("Lowercase: ", low_count)        

word = input("enter a sentence or word: ")    

case(word)