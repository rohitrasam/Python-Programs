class Student1:

    school = 'HHS'   # class variable

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):     # instance method because it has self and we are passing an object
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):   # getters fetch the value
        return self.m1

    def set_m1(self, value):  # setters set the value
        self.m1 = value

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print('This is a student class')


s1 = Student1(34, 34, 67)
s2 = Student1(78, 90, 21)
print(s1.get_m1())
print(s1.avg())
print(s2.avg())
print(s1.getSchool())
print(Student1.getSchool())

Student1.info()
