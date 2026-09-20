""" 1. Damage per second
    2. Hitpoints
    3. Training Cost
    4. Training Time
    5. Fav target
    6. Damage type
    7. Targets
    8. Housing Space
    9. Movement Speed"""


class Troops(object):

    def __init__(self, damage_per_second, hit_points, training_cost, training_time, fav_target, damage_type, targets,
                 housing_space, movement_speed, level, name=None):
        self.name = name
        self._damage_per_second = damage_per_second
        self._hit_points = hit_points
        self._training_cost = training_cost
        self._training_time = training_time
        self._fav_target = fav_target
        self._damage_type = damage_type
        self._targets = targets
        self._housing_space = housing_space
        self._movement_speed = movement_speed
        self._level = level

    def __str__(self):
        return "Name: {0.name}\nDamage per second: {0._damage_per_second}\nHit points: {0._hit_points}\n\
                Training Cost: {0._training_cost}\nTraining Time: {0._training_time}\n\
                    Favorite Target: {0._fav_target}\nDamage Type: {0._damage_type}\nTargets: {0._targets}\n\
                        Housing Space: {0._housing_space}\nMovement Speed: {0._movement_speed}, Level: {0._level}".format(self)


class Barbarian(Troops):

    def __init__(self, damage_per_second=23, hit_points=95, training_cost=150, training_time=5, fav_target="Any",
                 damage_type="Single Target", targets='Ground',
                 housing_space=1, movement_speed=16, level=1, name="Barbarian"):
        super().__init__(damage_per_second, hit_points,
                         training_cost, training_time, fav_target, damage_type, targets,
                         housing_space, movement_speed, level, name)

    def upgrade(self):
        self._level += 1
        self._damage_per_second += 20
        self._hit_points += 15
        self._training_cost += 50


class Archers(Troops):

    def __init__(self, damage_per_second=20, hit_points=40, training_cost=300, training_time=6, fav_target="Any",
                 damage_type="Single Target", targets='Ground & Air',
                 housing_space=1, movement_speed=24, name="Archers"):
        self._damage_per_second = damage_per_second
        self._hit_points = hit_points
        self._training_cost = training_cost
        self._training_time = training_time
        self._fav_target = fav_target
        self._damage_type = damage_type
        self._targets = targets
        self.housing_space = housing_space
        self._movement_speed = movement_speed
        self._level = 1
        super().__init__(name=name, damage_per_second=self._damage_per_second, hit_points=self._hit_points,
                         training_cost=self._training_cost, training_time=self._training_time,
                         fav_target=fav_target, damage_type=damage_type, targets=targets,
                         housing_space=housing_space, movement_speed=movement_speed, level=self._level)

    def upgrade(self):
        self._level += 1
        self._damage_per_second += 15
        self._hit_points += 10
        self._training_cost += 50


class Giants(Troops):

    def __init__(self, damage_per_second=31, hit_points=720, training_cost=2250, training_time=30,
                 fav_target="Defenses",
                 damage_type="Single Target", targets='Ground',
                 housing_space=5, movement_speed=12, name="Giants"):
        self._damage_per_second = damage_per_second
        self._hit_points = hit_points
        self._training_cost = training_cost
        self._training_time = training_time
        self._fav_target = fav_target
        self._damage_type = damage_type
        self._targets = targets
        self.housing_space = housing_space
        self._movement_speed = movement_speed
        self._level = 1
        super().__init__(name=name, damage_per_second=self._damage_per_second, hit_points=self._hit_points,
                         training_cost=self._training_cost, training_time=self._training_time,
                         fav_target=fav_target, damage_type=damage_type, targets=targets,
                         housing_space=housing_space, movement_speed=movement_speed, level=self._level)

    def upgrade(self):
        self._level += 1
        self._damage_per_second += 12
        self._hit_points += 22
        self._training_cost += 75


class Goblin(Troops):

    def __init__(self, damage_per_second=32, hit_points=56, training_cost=100, training_time=7,
                 fav_target="Resources(Damage x2)",
                 damage_type="Single Target", targets='Ground',
                 housing_space=1, movement_speed=32, name="Goblin"):
        self._damage_per_second = damage_per_second
        self._hit_points = hit_points
        self._training_cost = training_cost
        self._training_time = training_time
        self._fav_target = fav_target
        self._damage_type = damage_type
        self._targets = targets
        self.housing_space = housing_space
        self._movement_speed = movement_speed
        self._level = 1
        super().__init__(name=name, damage_per_second=self._damage_per_second, hit_points=self._hit_points,
                         training_cost=self._training_cost, training_time=self._training_time,
                         fav_target=fav_target, damage_type=damage_type, targets=targets,
                         housing_space=housing_space, movement_speed=movement_speed, level=self._level)

    def upgrade(self):
        self._level += 1
        self._damage_per_second += 10
        self._hit_points += 15
        self._training_cost += 50


class WallBreaker(Troops):

    def __init__(self, damage=43, hit_points=53, training_cost=1400, training_time=15,
                 fav_target="Walls(Damage x40)",
                 damage_type="Area Splash", targets='Ground',
                 housing_space=2, movement_speed=24, name="Wall Breaker"):
        self._damage = damage
        self._hit_points = hit_points
        self._training_cost = training_cost
        self._training_time = training_time
        self._fav_target = fav_target
        self._damage_type = damage_type
        self._targets = targets
        self.housing_space = housing_space
        self._movement_speed = movement_speed
        self._level = 1
        super().__init__(name=name, damage_per_second=self._damage, hit_points=self._hit_points,
                         training_cost=self._training_cost, training_time=self._training_time,
                         fav_target=fav_target, damage_type=damage_type, targets=targets,
                         housing_space=housing_space, movement_speed=movement_speed, level=self._level)

    def upgrade(self):
        self._level += 1
        self._damage_per_second += 5
        self._hit_points += 10
        self._training_cost += 80


class Balloon(Troops):

    def __init__(self, damage_per_second=162, hit_points=545, training_cost=4500, training_time=30,
                 fav_target="Defenses",
                 damage_type="Area Splash", targets='Ground',
                 housing_space=5, movement_speed=10, name="Balloon"):
        self._damage_per_second = damage_per_second
        self._hit_points = hit_points
        self._training_cost = training_cost
        self._training_time = training_time
        self._fav_target = fav_target
        self._damage_type = damage_type
        self._targets = targets
        self.housing_space = housing_space
        self._movement_speed = movement_speed
        self._level = 1
        super().__init__(name=name, damage_per_second=self._damage_per_second, hit_points=self._hit_points,
                         training_cost=self._training_cost, training_time=self._training_time,
                         fav_target=fav_target, damage_type=damage_type, targets=targets,
                         housing_space=housing_space, movement_speed=movement_speed, level=self._level)

    def upgrade(self):
        self._level += 1
        self._damage_per_second += 23
        self._hit_points += 80
        self._training_cost += 100


class Wizard(Troops):

    def __init__(self, damage_per_second=185, hit_points=175, training_cost=3000, training_time=30,
                 fav_target="Any",
                 damage_type="Area Splash", targets='Ground & Air',
                 housing_space=4, movement_speed=16, name="Wizard"):
        self._damage_per_second = damage_per_second
        self._hit_points = hit_points
        self._training_cost = training_cost
        self._training_time = training_time
        self._fav_target = fav_target
        self._damage_type = damage_type
        self._targets = targets
        self.housing_space = housing_space
        self._movement_speed = movement_speed
        self._level = 1
        super().__init__(name=name, damage_per_second=self._damage_per_second, hit_points=self._hit_points,
                         training_cost=self._training_cost, training_time=self._training_time,
                         fav_target=fav_target, damage_type=damage_type, targets=targets,
                         housing_space=housing_space, movement_speed=movement_speed, level=self._level)

    def upgrade(self):
        self._level += 1
        self._damage_per_second += 20
        self._hit_points += 30
        self._training_cost += 150


class Army_camp:

    def __init__(self):
        self._army_camp = []
        self._capacity = 20
        self._level = 1
        self._counter = 0

    def add_troops(self, troop, unit):
        for i in range(unit):
            if self._counter < self._capacity:
                self._army_camp.append(troop)
                self._counter += troop.housing_space
            else:
                print("Army camp is full. Please upgrade your camp")
                break

    def show_troops(self):
        hero_count = set(self._army_camp)
        if len(self._army_camp) > 0:
            for troops in hero_count:
                print("{0} X{1}".format(troops.name, self._army_camp.count(troops)))
            print("{}/{}".format(self._counter, self._capacity))
        else:
            print("Army camp is empty")

    def upgrade(self):
        self._capacity += 20
        self._level += 1


class Barracks:
    _level = 1
    _army_camp = Army_camp()

    def __init__(self, args):
        self._args = args
        if len(self._args) > 0:
            self._add_troops(self._args)

    def _add_troops(self, args):
        for troops in args:
            for i in troops:
                troop, unit = i
                self._army_camp.add_troops(troop, unit)

    def show_troops(self):
        self._army_camp.show_troops()

    def upgrade(self):
        self._level += 1


def available_troops(args):
    print("Available troops: ")
    for index, keys in enumerate(args.keys()):
        print('{}: {}'.format(index + 1, keys))


if __name__ == '__main__':
    list_of_troops = {"Barbarian": Barbarian(),
                      "Archer": Archers(),
                      "Giant": Giants(),
                      "Goblin": Goblin(),
                      "Wall Breaker": WallBreaker(),
                      "Balloon": Balloon(),
                      "Wizard": Wizard()}
    available_troops(list_of_troops)
    quit_ = False
    army = []
    while not quit_:
        name_, units = input("Enter name of the troops and number of troops(0 0 to quit.)").split()
        if name_ is '0':
            quit_ = True
            barracks = Barracks(army)
            barracks.show_troops()
            break
        army.append((list_of_troops[name_], int(units)))
