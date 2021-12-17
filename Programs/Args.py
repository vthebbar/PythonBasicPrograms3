# Use of *args (Arbitrary number of arguments)

def calcSum(*args):
    res=0
    for x in args:
        res=res+x
    return res


result1 = calcSum(10,20,30,40)
print(result1)

result2 = calcSum(100,200)
print(result2)