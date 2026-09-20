class Wing:

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("I can fly")
        elif self.ratio == 1:
            print("Flapping hard to fly")
        else:
            print("I can't fly")


class Duck():

    def __init__(self) -> None:
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle waddle")
    
    def swim(self):
        print("let's swim")

    def quack(self):
        print("Quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def walk(self):
        print("I waddle too")
    
    def swim(self):
        print("Water's chilly")
    
    def quack(self):
        print("I cannot quack LOL")


# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()


if __name__ == '__main__':
    donald = Duck()
    donald.fly()
    # test_duck(donald)

    # percy = Penguin()
    # test_duck(percy)
    