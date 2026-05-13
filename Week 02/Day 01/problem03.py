# largest element

nums = [1, 3, 4, 2, 9, 6]
# print(max(nums))

largest = nums[0]

for i in nums:
    if i > largest:
        largest = i

print(largest)