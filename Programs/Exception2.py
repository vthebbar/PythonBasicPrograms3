# To raise exception using raise key word


a=10
b=0

if b == 0:
    raise ZeroDivisionError
else:
    res=a/b
    print(res)