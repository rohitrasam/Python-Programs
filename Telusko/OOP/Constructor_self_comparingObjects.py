class Computer:

    def __init__(self):
        self.name = 'Rohit'
        self.age = 28

    def update(self):
        self.age = 30

    def compare(self, other):   # self = c1, other = c2
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()

c1.update()

if c1.compare(c2):
    print('They are same')
else:
    print('They are diff')

print(c1.name)
print(c2.name)

