class B:
    def fun1(self):
        self.a=int(input("Enter the a value is::"))
        print("This is Base Class")
class D(B):
    def fun2(self):
        print("This is Derived class",self.a)
f1=D()
f1.fun1()
f1.fun2()

class B:
    def fun1(self):
        self.a=int(input("Enter the a value is::"))
        print("This is Base class")
class D(B):
    def fun2(self):
        print("This is Derived class",self.a)
class D1(D):
    def fun3(self):
        print("This is Derived class-1",self.a)
f1=D1()
f1.fun1()
f1.fun2()
f1.fun3()

class B1:
    def fun1(self):
        self.a=int(input("Enter the a value is::"))
class B2:
    def fun2(self):
        self.b=int(input("Enter the b value is::"))
class D1(B1,B2):
    def display(self):
        c=self.a+self.b;
        print("Your value is::",c)
f1=D1()
f1.fun1()
f1.fun2()
f1.display()
