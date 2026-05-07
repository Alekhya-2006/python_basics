word = input("enter a word: ")

count = 0

for ch in word:
    if(ch == 'a' or
       ch == 'e' or
       ch == 'i' or 
       ch == 'o' or 
       ch == 'u'):
        count += 1

print(f'Number of vowels in {word} is {count}')   