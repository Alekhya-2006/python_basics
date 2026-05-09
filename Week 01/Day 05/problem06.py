# continuesly input a number n and print positive or negative
# Until the user enters "Quit"

while True:

    n = input("Enter a number (or Quit) : ")
    
    if n == "Quit":
        print("Successfully Quit") 
        break

    n = int(n)

    if n > 0:
        print("Positive")

    elif n < 0:
        print("negative")

    else:
        print("Zero") 