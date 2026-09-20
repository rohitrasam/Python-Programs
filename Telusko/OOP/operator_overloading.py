a = '5'
b = '6'
print(a + b)

# behind the scenes
print(str.__add__(a, b))


class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)

        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2  # variable
        r2 = other.m2 + other.m2  # variable
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(69, 420)  # object
s2 = Student(96, 440)  # object
s3 = s1 + s2   # -> Student.__add__(s1, s2)  self = s1, other = s2

print(s3.m1)

if s1 > s2:
    print('s1 wins')
else:
    print('s2 wins')

print(s1.__str__())  # to print the values of s1 object override __str__()
# print(s1)  # will give an error as it is returning a non-string value, use ".format" to remove the error
print(s2)
