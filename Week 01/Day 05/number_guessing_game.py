# Number guessing game

act_num = 20

while True:

    num = int(input("Guess the number: "))

    if num == act_num:
        print("Oh my God! It's Correct.")
        print("How did you guess it?")
        break

    elif num > act_num:
        print("Too high")

    else:
        print("Too low")