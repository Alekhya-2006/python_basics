nums = [-2, 9, -8, 0, -7, 7, -89]
updated_nums = [0 if val < 0 else val for val in nums]

print(nums)
print(updated_nums)

# Output: [0, 9, 0, 0, 0, 7, 0]