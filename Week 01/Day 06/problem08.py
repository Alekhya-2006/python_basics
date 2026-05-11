# remove spaces from string

def remove_spaces(word):
    sen = ""

    for i in word:

        if i != " " :
            sen = sen + i

    return sen       

sentence = input("write sentence: ")

print(remove_spaces(sentence))