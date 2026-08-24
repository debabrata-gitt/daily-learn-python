from abc import ABC, abstractmethod


class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class square(abstract):
    def __init__(self,side):
        self.side=side


class circle(abstract):
    def __init__(self,radious):
        self.radious=radious



    def perimeter(self) :
        print("I Have Created.")


    def area(self):
        print("I Have Created This.")    


obj=circle(7)   
   