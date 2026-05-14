# count frequency of characters

word = input("Enter a word: ")
unique_chars = set(word)
freq = {}

for i in unique_chars:
    count = 0
    for j in word:
        if j == i:
            count += 1
    freq[i] = count    

print(freq)