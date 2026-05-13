# smallest element

nums = [3, 4, 1, 2, -9, 9, 6]
# print(min(nums))

smallest = nums[0]

for i in nums:
    if i < smallest:
        smallest = i

print(smallest)