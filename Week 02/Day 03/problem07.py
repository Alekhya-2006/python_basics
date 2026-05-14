# check subset

nums = {1, 2, 3, 4, 5, 6, 7}
sub_nums = {1, 8, 5}

# print(sub_nums.issubset(nums))

n = 0
for i in sub_nums:
    if i in nums:
        n += 1

if n == len(sub_nums):
    print("subset")
else:
    print("not subset")    