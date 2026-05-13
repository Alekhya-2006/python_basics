# count frequency of element

def freq(lst, n):

    count = 0
    found = False

    for i in lst:

        if i == n:
            count += 1
            found = True

    if not found:
        print("not found")     

    else:
        print(f'frequency of {n} is {count}')       

nums = [1, 4, 7, 3, 4, 8, 8, 10, 8, 9] 
num = int(input("enter a number: ")) 

freq(nums, num)