import random


class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1) -> None:
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("{0._name} took {1} points damage and has {0._hit_points} left".format(self, damage))
        else:
            self._lives -= 1
            if self._lives > 0:
                print("{0._name} lost a life".format(self))
            else:
                print("{0._name} is dead.".format(self))
                self._alive = False
    
    def __str__(self) -> str:
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}".format(self)


class Symbiote(Enemy):
    
    def __init__(self, name):
         super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print("We are {0._name}".format(self))


class Vampyre(Enemy):

    def __init__(self, name) -> None:
        super().__init__(name, hit_points=12, lives=3)
    
    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print("*** {0._name} dodges ***".format(self))
            return True
        return False


class VampyreKing(Vampyre):

    def __init__(self, name) -> None:
        super().__init__(name)  # super should be declared before any other statements in the `__init__` method
        self._hit_points = 140
    
    def take_damage(self, damage):
        super().take_damage(damage / 4)

        