# Remove elements from set

nums_set = {1, 3, 5, 7, 9, 11, 13, 15}

n = int(input("Enter the number you want to remove: "))

if n in nums_set:

    nums_set.remove(n)
    print("Element removed successfully")

else:
    print("Element not found")

print(nums_set)