# count unique characters in string

word = input("Enter the word: ")

unique_chars = set()
for i in word:
    unique_chars.add(i)

print("Number of unique characters:", len(unique_chars))
print("Unique characters:", unique_chars)