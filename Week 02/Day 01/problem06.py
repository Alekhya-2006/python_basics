# search element in list

def search_element(lst, n):
    idx = 0
    found = False
    for i in lst:

        if i == n:
            print(f'{n} found at index {idx}')
            found = True
            break

        idx += 1
    if not found:
        print("not found")

nums = [1, 3, 5, 7, 9]        

num = int(input("enter the number u wanna search: "))

search_element(nums, num)