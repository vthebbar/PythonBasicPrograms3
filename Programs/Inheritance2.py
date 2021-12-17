# Multiple inheritance

class A:

    def methodA(self):
        print("Class A Method")

    def display(self):
        print("Display A")

class B:

    def methodB(self):
        print("Class B Method")

    def display(self):
        print("Display B")

class C(B,A):

    def methodC(self):
        print("Class C Method")



obja = A()
objb = B()
objc = C()

obja.display()
objb.display()
objc.display() # Display method will be called from ...
            #... first specified class in inheritance (Based on Method Resolution Order(MRO) )

#MRO
print(C.mro())
print(B.mro())
print(A.mro())


obja.methodA()
objb.methodB()
objc.methodC()