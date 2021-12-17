# Lambda function is a anonymous function, which accepts single expression

# Lambda function to find sum of 3 numbers

total = lambda a, b, c: a+b+c
res=total(10,20,30)
print(res)


# Find square of number using lambda function

square = lambda x : x*x
result = square(4)
print(result)

list1 =[1,2,3,4,5]
print("*********")
for i in list1:
    print(square(i))