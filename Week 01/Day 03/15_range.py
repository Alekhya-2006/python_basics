# range() : Sequence generator
# range(start, stop, step)
# default step is +1

for i in range(10):
    print(i) # 0 to 9

print("\n")

for i in (range(2,10)):
    print(i) # 2 to 9

print("\n")

for i in (range(1,10,2)): 
    # starts from 1, increases by 2 each time, stops before 10
    print(i) # 1, 3, 5, 7, 9   