# type coversion is implicit, which means python interpreter converts itself automatically

a = 10
b = 5
print(a / b, type(a / b)) # float

ans1 = 5 + 10.0
print(ans1, type(ans1)) # float

# type casting is explicit, which is noot done automatically
# done by developer

ans2 = int(5 + 10.0)
print(ans2, type(ans2)) # int

val = "101"
print(val, type(val)) # 101 <class 'str'>

val = int("101")
print(val, type(val)) # 101 <class 'int'>

val = bool("101")
print(val, type(val)) # True <class 'bool'>
# In boolean, zero is false
# and every non-zeroes are True