# Dictionary

# create dictionary  (method1)
employees = {10:"Ram",20:"Raj",30:"Bhim","ID1":"Ramu", "ID2":"Ravi"}
print(employees)

# create dictionary using constructor - (method2)
users = dict(key1="value1",key2="value2", key3="value3")   # key should not in double quote in this type
print(users)

# create dictionary using constructor (method3)
names = dict([(10,"Ravi"),(20,"Ram"),(30,"Bhim")])
print(names)

# Nested dictionary
teams = {"dev":{"java":"Raj","python":"Vishwa"},"QA":{"manual":"Asha","Automation":"Vish"}, "devops":"Ramu", "acct":"shubha"}
print(teams)
print("*******************************")
print(teams["dev"])
print(teams["dev"]["java"])
print(teams["dev"]["python"])
print("*******************************")
x = teams.get("QA")
print(x)
y = teams.get("QA").get("Automation")
print(y)

print("*******************************")
# List inside dictionary
dict1 = {"Group1":"Raju","Group2":["Ram","Bhim",'Shyam']}
print(dict1["Group2"][1])

print("*******************************")
# Add new item to dictionary (need to use new key)

dict1["Group3"] ="Neema"
print(dict1)

# Change/Modify/update existing value (need to use existing key
dict1["Group3"] = "Shree"
print(dict1)

print("*******************************")
print(len(employees))

print(employees.keys())  # To get only keys
print(employees.values()) # To get only values
print(employees.items()) # To get key-value pair as a list of tuples

print("*******************************")
# delete a particular item in dictionary

print(employees)
del employees["ID1"]
print(employees)


# Delete entire dictionary
del employees
# print(employees) -> NameError: name 'employees' is not defined