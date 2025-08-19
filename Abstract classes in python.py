from abc import ABC,abstractmethod
class polygon(ABC):
    def noofsides(self):
        pass
class Triangle(polygon):
    def noofsides(self):
        print("I have 3 side")
class Hexagon(polygon):
    def noofsides(self):
        print("I have 6 side")
R=Triangle()
R.noofsides()
K=Hexagon()
K.noofsides()

    
