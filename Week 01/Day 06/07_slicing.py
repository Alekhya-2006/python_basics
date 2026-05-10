# syntax -->  str[start index: end index]
# ending index not included
# default starting index is 0
# default ending index is len(str)

word = "python"

print(word[2:4]) # th
print(word[3: ]) # empty space indicates goes till string end
print(word[3: len(word)]) # same as above
print(word[:]) # from 0 to till end