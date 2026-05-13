# reverse a list

nums = [1, 3, 4, 2, 9, 6]
# nums.reverse()
# print(nums)

reverse_nums = []
for i in nums:
    reverse_nums.insert(0, i)
print(reverse_nums)