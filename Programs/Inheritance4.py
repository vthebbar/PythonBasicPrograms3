# Hybrid Inheritance - combination on Multiple and multilevel

class A:
    def methodA(self):
        print("Class A - Method A")

class B(A):
    def methodB(self):
        print("Class B - Method B")


class C(B):
    def methodC(self):
        print("Class C - Method C")

class D:
    def methodD(self):
        print("Class D - Method D")

class E(C,D):
    def methodE(self):
        print("Class E - Method E")

obje = E()
obje.methodA()
obje.methodB()
obje.methodC()
obje.methodD()
obje.methodE()