class sample:
    def fun1(self):
        print("This is fun1")
f1=sample()
f1.fun1()

class sample:
    def fun1(self):
        print("This is fun1")
    def fun2(self):
        pid=int(input("Enter the pid is::"))
        print("your value is::",pid)
f1=sample()
f1.fun1()
f1.fun2()

class Demo:
    def get1(self,name):    
        print("Get1 fun is::",name)
    def get2(self):
        self.age=int(input("Enter the age is::"))
    def display(self):
        print("your age is::",self.age)
d1=Demo()
d1.get1("sdlc")
d1.get2()
d1.display()
    
