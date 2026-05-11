# count words in a sentencs:

def count_words(sen):
    count = 0
    for i in sen:
        if i == " ":
            count += 1
    return count + 1        

sentence = input("enter a sentence: ")

print("Number of words = ",count_words(sentence))