class Car:

    wheels = 4  # Class variable because it is inside a class

    def __init__(self, mil=10, com='default'):
        self.mil = mil   # instance variables because they are inside init
        self.com = com


c1 = Car(20, "Mercedes")
c2 = Car()

c1.wheels = 5

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)
