
# To find builtin functions
print(dir(__builtins__))

# Use of Zip function
list1=["India","USA","UK","UAE"]
list2=["Delhi","Washington","London","Dubai"]

zipdata = zip(list1,list2)
print(zipdata) # Returns memory location

data = list(zipdata)
print(data)  # [('India', 'Delhi'), ('USA', 'Washington'), ('UK', 'London'), ('UAE', 'Dubai')]


# Unzip - tuple unpacking
a,b = zip(*data)  # First value of each tuple will store in a and second value in b
print(a,b)  # ('India', 'USA', 'UK', 'UAE') ('Delhi', 'Washington', 'London', 'Dubai')


# Single iterable as a parameter to zip

list3=[10,20,30,40]
zipdata2 = zip(list3)
print(zipdata2)
data2 = list(zipdata2)
print(data2)

#
x = zip(*data2)
print(x)