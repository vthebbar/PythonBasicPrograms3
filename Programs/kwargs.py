# use of **kwargs (Arbitrary number of keyword arguments)

def getValues(**kwargs):
    for x,y in kwargs.items():
        print("key=", x, " Value=",y)


getValues(name="Raj", address="Blore", id=1234)

getValues(Country="India", Capital="New Delhi", Phonecode="+91")

getValues(fname="Tom", lname="kumar")
