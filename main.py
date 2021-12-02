# Player creation
import random
import sys


def player_creator():
    global p
    def pick_name():
        name = input("What is your name?:\n")
        if 2 < len(name) > 16:
            print("Naming Rules:\n1: Less than 16 characters and more than 2.")
            pick_name()
        p.name = str(name)

    def pick_sex():
        sex = input("Pick a sex:\n"
                    "M: Male\n" 
                    "F: Female\n"
                    )
        sex = str(sex.upper())
        if sex == "F":
            sex = "Female"
            p.sex = str(sex)

        elif sex == "M":
            sex = "Male"
            p.sex = str(sex)

        else:
            print("Please enter a correct sex 'M' or 'F'")
            print(sex.upper())
            pick_sex()

    def pick_class():
        clist = ["Rogue", "Warrior", "Mage"]
        print("Pick a class. (Type help for more information)", "Rogue", "Warrior", "Mage", sep='\n', end='\n')
        c = input()
        c = c.capitalize()
        if c == "Help":
            print("Classes are a job and the way you will live out your life in the world")
            pick_class()
        elif (c in clist):
            p.cl = c
            build_class()
        else:
            print("Please enter a proper class")
            pick_class()

    def build_class():
        if p.cl == 'Rogue':
            p.level = 1
            p.hpMod = 30
            p.dmgMod = 3
            p.Equ = []
            p.Inv = [p.Equ]
            p.maxHP = + (p.level * p.hpMod)
            Game.equip_stats(Game) #func to get total modified dmg
            p.entType = 'player'
            p.stats = {'Name': p.name, 'Sex': p.sex, 'Class': p.cl, 'Level': p.level, 'Health': p.maxHP, 'Damage': p.dmg}
        elif p.cl == 'Warrior':
            p.level = 1
            p.hpMod = 50
            p.dmgMod = 1
            p.Equ = []
            p.Inv = [p.Equ]
            p.maxHP = + (p.level * p.hpMod)
            Game.equip_stats(Game) #func to get total modified dmg
            p.entType = 'player'
            p.stats = {'Name': p.name, 'Sex': p.sex, 'Class': p.cl, 'Level': p.level, 'Health': p.maxHP, 'Damage': p.dmg}
        elif p.cl == 'Mage':
            p.level = 1
            p.hpMod = 10
            p.dmgMod = 5
            p.Equ = [Items.Glove, Items.Weapon, Items.Boots, Items.Armor]
            p.Inv = [p.Equ]
            p.maxHP = + (p.level * p.hpMod)
            Game.equip_stats(Game) #func to get total modified dmg
            p.entType = 'player'
            p.stats = {'Name': p.name, 'Sex': p.sex,
                       'Class': p.cl, 'Level': p.level,
                       'Health': p.maxHP, 'Damage': p.dmg,
                       'Defence': p.dr
                       }
        else:
            p.level = 1
            p.hpMod = 10
            p.dmgMod = 1
            p.Equ = []
            p.Inv = [p.Equ]
            p.maxHP = + (p.level * p.hpMod)
            Game.equip_stats(Game) #func to get total modified dmg
            p.entType = 'player'
            p.stats = {'Name': p.name, 'Sex': p.sex, 'Class': p.cl, 'Level': p.level, 'Health': p.maxHP, 'Damage': p.dmg}


    #Call the functions to create player

    pick_name()
    pick_sex()
    pick_class()
    Game.pls = [p]



#Player Object Template
class Player:
    def __init__(self,  name, sex, cl, level, hpMod, maxHP, dmgMod, dmg, dr, entType, speed=1):
        self.name = name
        self. sex = sex
        self.cl = cl
        self.level = level
        self.hpMod = hpMod
        self.dmgMod = dmgMod
        self.maxHP = maxHP
        self.dmg = dmg
        self.dr = dr
        self.entType = entType
        self.speed = speed
    Equ = []
    Inv = []
    stats = {}


class Skills:

    def stab(self):
        name = "Stab"
        Game.m.health -= Game.damage_calc(Game, p.dmg)
        print(p.name + " used " + name)


class Items:

    class Glove:
        name = "Glove"
        dur = 10
        atk = 5

    class Weapon:
        name = "Weapon"
        dur = 10
        atk = 20

    class Boots:
        name = "Boots"
        dur = 10
        dr = 5

    class Armor:
        name = "Armor"
        dur = 10
        dr = 10


class Game:

    def __init__(self, floor, deaths, kills):
        self.kills = kills
        self.deaths = deaths
        self.floor = floor
    pls = []
    gcr = 0

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
        self.monster_gen(Game)
        self.show_stats(Game.m)
        pturn = False
        if p.speed > Game.m.speed:
            pturn = True
        elif p.speed < Game.m.speed:
            pturn = False
        #Prompt the player with there turn


    def combat_turn(self):
        return

    def monster_gen(self):
        Game.m = self.Monster(random.randint(1, p.stats['Level'] + 1), 2, entType='mob', speed=1)
        Game.m.name = 'Monster'  # Placeholder for random monster name picker
        # Buffing from Player Challenge Rating
        Game.m.health *= Game.m.level
        Game.m.dmg += Game.m.level


    def show_stats(t):
        print("-" * 16)
        # t is the targeted object
        if t.entType == "player":
            print(t.name + "'s" + " Stats")
            for a, b in p.stats.items():
                print(str(a), end=': ' + str(b) + '\n')

        elif t.entType == 'mob':
            print(t.name + "'s" + " Stats")
            for a, b in Game.m.__dict__.items():
                if a == 'loot':
                    continue
                elif a == 'entType':
                    continue
                print(a.capitalize() + ':', str(b))
        print("-" * 16)

    #calculates the game
    def damage_calc(self, d):
        return d  #Place holder for more complex dmg calc

    def equip_stats(self):
        dm = p.dmgMod
        a = 0
        d = 0
        al = ['Weapon', 'Glove']
        dl = ['Boots', 'Armor']
        for b in p.Equ:
            if b.name in al:
                a += b.atk
                continue
            elif b.name in dl:
                d += b.dr
                continue
        p.dmg = a * dm
        p.dr = d

    class Monster:
        def __init__(self, health, dmg, entType, speed):
            self.health = health
            self.dmg = dmg
            self.loot = []
            self.level = self.health + self.dmg
            self.entType = entType
            self.speed = speed

    # Start game
    def setup_game(self):
        self.game_start(Game)


#New player
def new_player():
    global p
    #Clear everything
    p = Player('', '', '', 0, 0, 0, 0, 0, 0, 'player', 1)
    p.Equ = []
    p.Inv = []
    p.stats = {}
    #Start Character creation
    player_creator()


if __name__ == '__main__':
    new_player()
    Game.game_start(Game)
    Game.show_stats(p)



