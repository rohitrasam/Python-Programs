class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        s = 0
        if a is not None and b is not None and c is not None:
            s = a + b + c
        elif a is not None and b is not None:
            s = a + b
        else:
            s = a
        return s


s1 = Student(69, 420)

print(s1.sum(6))
