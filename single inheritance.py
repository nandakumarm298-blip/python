
class B:
    def fun1(self):
        self.name=input("Enter the name is::")
        print("This is base class",self.name)
class D(B):
    def fun2(self):
        print("This is derived class",self.name)
f1=D()
f1.fun1()
f1.fun2()


class Animal:
    def eat(self):
        self.age=int(input("Enter the age is::"))
        print("Animal is eating")
class Bird:
    def fly(self):
        print("Bird is flying")
class Eagle(Animal,Bird):
    def hunt(self):
        print("Eagle is hunting",self.age)
e1=Eagle()
e1.eat()
e1.fly()
e1.hunt()        

def fun1():
    print("This is func1")
    a=int(input("Enter the a value is::"))
    print("Your value is::",a)
def fun2():
    print("This is func2")
fun1()
fun2()

def fun1():
    print("This is func1")
    for i in range (0,10,1):
        print("I value is::",i)
def fun2():
    print("This is func2")
fun1()
fun2()


def fun1():
    print("welcome")
def fun2():
    pass
fun1()
