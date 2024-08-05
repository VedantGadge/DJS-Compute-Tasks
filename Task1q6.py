class Commander:
    def __init__(self,name,rank,weight,height,age):
        self.name=name
        self.rank=rank
        self.weight=weight
        self.height=height
        self.age=age

    def calculate_danger(self):
        lvl = int((self.weight+self.height)/self.age)
        print('Danger level =',lvl)

c = Commander('Zerzoza',5,250,9,30)
c.calculate_danger()

'''
Instance Reference:

self is a conventional name used in Python to refer to the instance of the class. It allows access to the attributes and methods of the class from within the class itself.
Initialization:

In the __init__ method, self refers to the instance being created. When you create an object c with c = Commander('Zerzoza', 5, 250, 9, 30), self in __init__ refers to this new Commander instance.
Attributes like self.name, self.rank, self.weight, self.height, and self.age are assigned values based on the arguments passed during object creation.
Method Access:

Within other methods (e.g., calculate_danger), self is used to access the instance's attributes (self.weight, self.height, self.age) and to call other methods or manipulate the instance data.
'''