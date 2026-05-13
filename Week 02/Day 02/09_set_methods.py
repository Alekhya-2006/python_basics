# set methods

s1 = {1, 5, 3, 9, 2}
print(s1)

s1.add(4) #adds 
s1.remove(1) # removes 1
s1.pop() # removes a random value

print(s1)

s2 ={0, 3, -4, -2}

print("union =", s1.union(s2))
print("intersection =", s1.intersection(s2))