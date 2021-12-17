# Strings

str1 = "My name is Vishwa, I love Python"

# length
print(len(str1))

# Indexing
print(str1.index("V")) # Index number of V, (index starts from 0)

# Split
print(str1.split(" ")) # split based on space


# Slicing
print(str1[0:3]) # index 0 to 2

#step count
print(str1[::5]) # print every 5th character, starts from 0 till end of string

# Reverse string using step count
print(str1[::-1])


# Escape sequence characters
test = "My\tname\tis\n\"Vishwa\""
print(test)

# format method
name1="raj"
name2="ram"
name3="bhim"
test1 = "Names are: {} {} {}".format(name1, name2, name3)
print(test1)

# pass index number to print in different order
test2 = "Names are: {2} {1} {0}".format(name1,name2,name3)
print(test2)

# key, value pair with format method

test3 = "Numbers are:- {a} {c} {b}".format(a=10,b=20,c=30)
print(test3)

# f string / string literal

print(f"Names are -: {name1} {name2} {name3} ")