# Player creation
import random


def player_creator():
    def pick_name():
        name = input("What is your name?:\n")
        if 2 < len(name) > 16:
            print("Naming Rules:\n1: Less than 16 characters and more than 2.")
            pick_name()
        Player.name = str(name)

    def pick_sex():
        sex = input("Pick a sex:\n"
                    "M: Male\n" 
                    "F: Female\n"
                    )
        sex = str(sex.upper())
        if sex == "F":
            sex = "Female"
            Player.sex = str(sex)
            return
        elif sex == "M":
            sex = "Male"
            Player.sex = str(sex)
            return
        else:
            print("Please enter a correct sex 'M' or 'F'")
            print(sex.upper())
            pick_sex()

    def pick_class():
        print("Pick a class. (Type help for more information)", "Rouge", "Warrior", "Mage", sep='\n', end='\n')
        Player.cl = input()
        if Player.cl == "help":
            print("Classes are a job and the way you will live out your life in the world")
            pick_class()


    #Call the functions to create player
    pick_name()
    pick_sex()
    pick_class()
    Player.level = 1
    Game.pls = [Player]
    Player.stats = [Player.name, Player.sex, Player.cl, Player.level]


#Player Object Template
class Player:
    def __init__(self,  name, sex, cl, level):
        self.name = name
        self. sex = sex
        self.cl = cl
        self.level = level
        self.maxHP = level * hpMod

    stats = []

class Game:

    def __init__(self, floor, deaths, kills):
        self.kills = kills
        self.deaths = deaths
        self.floor = floor
    pls = []
    gcr = 0
    m = None

    def get_players_info(self):
        for x in self.pls:
            print('Welcome ' + x.name)
            self.gcr += x.level

    def game_start(self):
        g = Game(floor=1, deaths=0, kills=0)
        self.get_players_info(Game)
        print("Floor: " + str(g.floor))
        self.encounter(Game)

    def encounter(self):
        self.Monster.monster_gen(Game)


    class Monster:
        def __init__(self, health, dmg):
            self.health = health
            self.dmg = dmg
            self.loot = []
            self.level = self.health + self.dmg

        def monster_gen(self):
            m = Game.Monster(random.randint(1, Player.stats[3]), 2)
            #Buffing from Player Callenge Rating
            m.health *= m.level
            m.dmg += m.level

            for a, b in m.__dict__.items():
                if a == ('loot', []):
                    continue
                print(a.capitalize() + ':', str(b))


    # Start game
    def setup_game(self):
        self.game_start(Game)


#New player
def new_player():
    player_creator()


if __name__ == '__main__':
    new_player()
    Game.game_start(Game)
    for p in Player.stats:
        if p == Player.level:
            print("Level: " + str(p))
            continue
        print(p.capitalize(), end=' ')


