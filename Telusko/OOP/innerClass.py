class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()  # create an object of inner class Laptop

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i3'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Rohit', 69)
s2 = Student('Pearl', 96)

s1.show()
s2.show()

# lap1 = Student.Laptop()  # create object of inner class outside the outer class
