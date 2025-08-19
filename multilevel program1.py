class B:
    def fun1(self):
        self.name=input("This is derived class",self.name)
        print("This is base class",self.name)
class D(B):
    def fun2(self):
        print("This is derived class",self.name)
f1=D()
f1.fun1()
f2.fun2()
