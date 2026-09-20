from player import Player
from enemy import Enemy, Symbiote, Vampyre, VampyreKing

if __name__ == '__main__':

    # rohit = Player('Rohit')
    # print(f"{rohit}")
    # rohit.lives -= 1
    # print(rohit)
    # rohit.lives -= 1
    # print(rohit)
    # rohit.lives -= 1
    # print(rohit)
    # rohit.lives -= 1
    # print(rohit)

    # rohit.level = 2
    # print(rohit)
    
    # rohit.level += 5
    # print(rohit)

    # rohit.level = 3
    # print(rohit)

    # rohit.score = 500
    # print(rohit)

    # random_enemy = Enemy("Hammerhead", 12, 1)
    # print(random_enemy)

    # random_enemy.take_damage(4)
    # print(random_enemy)
    
    # random_enemy.take_damage(8)
    # print(random_enemy)
    
    # random_enemy.take_damage(9)
    # print(random_enemy)

    # venom = Symbiote("Venom")
    # print("Venom -> {}".format(venom))

    # # carnage = Symbiote("Carnage", 18, 1)
    # carnage = Symbiote("Carnage")
    # print('Carnage -> {}'.format(carnage))

    # # riot = Symbiote("Riot", 23)
    # riot = Symbiote("Riot")
    # print("Riot -> {}".format(riot))

    # venom.grunt()
    # carnage.grunt()
    # riot.grunt()

    # morbius = Vampyre("Morbius")
    # print(morbius)
    # morbius.take_damage(11)
    # print(morbius)
    # while morbius.alive:
    #     morbius.take_damage(4)
    #     print(morbius)
     
    dracula = VampyreKing("Dracula")
    print(dracula)
    dracula.take_damage(12)
    print(dracula)