# remove duplicates

nums = [1, 3, 4, 7, 2, 9, 6, 6, 4, 3, 3]

unique_nums = []

for i in nums:
    if i not in unique_nums:
        unique_nums.append(i)

print(unique_nums)