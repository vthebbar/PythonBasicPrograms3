# While loop is used to run piece of code multiple times, While loop is used when we do not know how many times
# ..code need to be run.
# While loop runs as long as given condition is true and once condition is false contorl comes out of the loop
# Need to initialize a loop variable before while loop and need to increment or decrement variable inside the loop

# example -
# While loop can be used with else, break, continue, pass

x=10

while x<=20:
    print(x)
    x+=1

print("**********")

y=10
while y>=0:
    print(y)
    y-=1


print("*****While loop with else ****")

a=0
while a<=5:
    print(a)
    a=a+1
else:
    print("Else part")


print("*****While loop with break ****")

b=0

while b<=5:
    print(b)
    b+=1
    if b==3:
        break

print("*****While loop with continue ****")

c=0
while c<=5:
    c += 1
    if c==3:
        continue
    print(c)

d=0
while d<=10:
    d+=1
    #print(d)
    pass   # does nothing , used when a piece of code is not ready and we can avoid syntax error by using pass statement
