# check list palindrome

lst = [1, 2, 3, 2, 1]

reverse = []
for i in lst:
    reverse.insert(0, i)

if lst == reverse:
    print("Palindrome")

else:
    print("Not Palindrome")    