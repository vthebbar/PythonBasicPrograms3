# For loop is used for running a piece of code multiple times. When we are using for loop we know how many times code..
#..to be run
# else statement can be used with for loop

list1=[10,20,"raj",40,90.99]

for l in list1:
    print(l)
else:
    print("out of for loop")


my_dict ={"name":"Ram","email":"abc@gmail.com","Phone":1234}

for x in my_dict:
    print(x)  # prints keys only

for y in my_dict.values():
    print(y)  # prints values only

for a in my_dict.items():
    print(a)  # prints key value pair as tuple

for m,n in my_dict.items():
    print(m)  # key
    print(n)   # value


list2=[(1,2,3),(10,20,30),(100,200,300)] # list of tuples

for i in list2:
    print(i[0])
    print(i[1])
    print(i[2])

for a,b,c in list2:  # Tuple unpacking of list of tuples
    print(a)
    print(b)
    print(c)

res= list(zip(*list2))
print(res)