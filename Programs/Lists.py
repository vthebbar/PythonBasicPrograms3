# Lists

list1 = [10,20,30,40,"Raj"]
list2 = [900,100,200,300,400,100]

# addition of lists
list3 = list1+list2
print(list3)

# slicing
print(list1[1:3])

# Append
list1.append(108)
print(list1)

# Extend
str1="Vishwa"
list1.extend(str1) # will append character by character
print(list1)

list1.extend(list2) # appends element by element
print(list1)

list1.append(list2)  # appends entire list as one element
print(list1)

# sort
list2.sort()
print(list2)

# count
print(list2.count(100))

# pop - removes last element
print(list1)
list1.pop()
print(list1)


# reverse
list1.reverse()
print(list1)

# Remove
list1.remove(10)
print(list1)
