 # frequency of a character:

def frequency(ch, word):
    count = 0

    for i in word:

        if i == ch:
            count += 1 

    return count        

sentence = input("write sentence or word: ")
char = input("which character do you want to count: ")

print(f"The number of {char}'s in the input is {frequency(char, sentence)}")