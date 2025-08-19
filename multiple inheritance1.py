class Animal:
    def eat(self):
        self.age=int(input("Enter the age is ::"))
        print("Animal is eating")
class Bird:
    def fly(self):
        print("Bird is flying")
class Eagle(Animal,Bird):
    def hunt(self):
        print("Eagle is hunting",self.age)
e1=Eagle()
e1=eat()
e1.fly()
e1.hunt()
