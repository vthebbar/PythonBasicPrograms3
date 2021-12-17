# sets

set1 = {10,20,"raj",10,20,"ram","bhim",100,200,100}
print(set1) # duplicate wil be rmeoved

# add element to set
set1.add(108)
print(set1)

# remove element from set
set1.remove(10)
print(set1)

# discard - remove if element is present, else does nothing
set1.discard(20)
print(set1)

set1.discard(20)
print(set1)

set1.pop()  # remove random element
print(set1)


# copy set

set2 = set1.copy()
print(set2)


# clear
set1.clear()
print(set1)

# length
print(len(set1))
print(len(set2))



# Convert list to set
list1 =[10,20,30,"ram"]
set3 = set(list1)
print(set3)


# convert tuple to set
tup1 = (10,20,"bhima","shiva",100)
set4 = set(tup1)
print(set4)