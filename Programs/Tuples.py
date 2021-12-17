# Tuples

# Create Tuple (method 1)
tup1 = (10,20,"raj","ram",40,"bhim")

print(tup1)

# Create Tuple using constructor (method 2)
tup2 = tuple([100,200,300,400,"raj"])
print(tup2)

l1 = [1,2,3,4,5,5,5,5]
tup3 = tuple(l1)
print(tup3)

print("*****************")
# Methods
print(tup3.count(5))  # count
print(tup3.index(5))  # first occurrence of 5

print(tup3[3])

#  tup3[0]="raj"   -> Tuples are immutable
print(len(tup3))
print("*****************")
# Convert tuple to set
s1 = set(tup3)
print(s1)

# convert tuple to list
l2 = list(tup3)
print(l2)