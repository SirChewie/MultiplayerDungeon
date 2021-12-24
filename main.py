# Player creation
import random
import sys

import main


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
            p.maxHP = p.level * p.hpMod
            p.currHealth = p.maxHP
            Game.equip_stats(Game) #func to get total modified dmg
            p.skills = [Skills.Stab]
            p.entType = 'player'
            p.stats = {'Name': p.name, 'Sex': p.sex,
                       'Class': p.cl, 'Level': p.level,
                       'Health': p.maxHP, 'Damage': p.dmg,
                       'Defence': p.dr}
        elif p.cl == 'Warrior':
            p.level = 1
            p.hpMod = 50
            p.dmgMod = 1
            p.Equ = []
            p.Inv = [p.Equ]
            p.maxHP = p.level * p.hpMod
            p.currHealth = p.maxHP
            Game.equip_stats(Game) #func to get total modified dmg
            p.skills = [Skills.Stab]
            p.entType = 'player'
            p.stats = {'Name': p.name, 'Sex': p.sex,
                       'Class': p.cl, 'Level': p.level,
                       'Health': p.maxHP, 'Damage': p.dmg,
                       'Defence': p.dr}
        elif p.cl == 'Mage':
            p.level = 1
            p.hpMod = 10
            p.dmgMod = 5
            p.Equ = [Items.Weapon, Items.Boots, Items.Armor]
            p.Inv = [p.Equ, Items.Glove]
            p.maxHP = p.level * p.hpMod
            p.currHealth = p.maxHP
            Game.equip_stats(Game) #func to get total modified dmg
            p.skills = [Skills.Stab]
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
            p.maxHP = p.level * p.hpMod
            p.currHealth = p.maxHP
            Game.equip_stats(Game) #func to get total modified dmg
            p.skills = [Skills.Stab]
            p.entType = 'player'
            p.stats = {'Name': p.name, 'Sex': p.sex,
                       'Class': p.cl, 'Level': p.level,
                       'Health': p.maxHP, 'Damage': p.dmg,
                       'Defence': p.dr}


    #Call the functions to create player

    pick_name()
    pick_sex()
    pick_class()
    Game.pls = [p]



#Player Object Template
class Player:
    def __init__(self,  name, sex, cl, level, hpMod, maxHP, currHealth, dmgMod, dmg, dr, entType, speed=1):
        self.name = name
        self. sex = sex
        self.cl = cl
        self.level = level
        self.hpMod = hpMod
        self.dmgMod = dmgMod
        self.maxHP = maxHP
        self.currHealth = currHealth
        self.dmg = dmg
        self.dr = dr
        self.entType = entType
        self.speed = speed
    Equ = []
    Inv = []
    stats = {}
    skills = []
    flee = False


class Items:
    itemlist = []

    def build_itemlist(self):
        self.itemlist = [self.Glove, self.Boots, self.Armor, self.Weapon]

    class Glove:
        name = "Glove"
        t = 'armor'
        dur = 10
        atk = 1

    class Weapon:
        name = "Weapon"
        t = 'weapon'
        dur = 10
        atk = 2

    class Boots:
        name = "Boots"
        t = 'armor'
        dur = 10
        dr = 1

    class Armor:
        name = "Armor"
        t = 'armor'
        dur = 10
        dr = 2


class Game:

    def __init__(self, floor, deaths, kills):
        self.kills = kills
        self.deaths = deaths
        self.floor = floor
    pls = []
    gcr = 0
    mnl = ['Slime']

    def get_players_info(self):
        for x in self.pls:
            print('Welcome ' + x.name)
            self.gcr += x.level

    def game_start(self):
        g = Game(floor=1, deaths=0, kills=0)
        self.get_players_info(Game)
        print("Floor: " + str(g.floor))
        Items.build_itemlist(Items)
        self.encounter(Game)

    def encounter(self):
        global m
        global p
        self.monster_gen(Game)
        self.show_stats(self, m)
        p.flee = False
        pturn = False
        if p.speed > m.speed:
            pturn = True
        elif p.speed < m.speed:
            pturn = False

        #Prompt the player with their turn
        if pturn == True:
            while 1 < 2:
                self.combat_turn(Game, p)
                print(p.currHealth)
                print(m.currHealth)
                #check if anyone died
                if p.currHealth <= 0 or p.flee:
                    if p.flee == True:
                        print("You flee combat")
                        break
                    else:
                        print("You have died")
                        break
                elif m.currHealth <= 0:
                    print("The Monster is has fainted")
                    break
                else:
                    pass
                #computer's turn
                self.combat_turn(Game, m)
                if p.currHealth <= 0 or p.flee:
                    if p.flee == True:
                        print("You flee combat")
                        break
                    else:
                        print("You have died")
                        break
                elif m.currHealth <= 0:
                    print("The Monster is has fainted")
                    break
                else:
                    pass
        #Monster goes first
        elif pturn == False:
            print('The Monster goes first!')
            while 1 < 2:
                # Computer takes a turn
                self.combat_turn(Game, m)
                print(p.name + "'s health " + str(p.currHealth))
                print(m.name + "'s health " + str(m.currHealth))
                #check if anyone died
                if p.currHealth <= 0 or p.flee:
                    if p.flee == True:
                        print("You flee combat")
                        break
                    else:
                        print("You have died")
                        break
                elif m.currHealth <= 0:
                    print("The Monster is has fainted")
                    break
                else:
                    pass
                self.combat_turn(Game, p)
                print(p.name + "'s health " + str(p.currHealth))
                print(m.name + "'s health " + str(m.currHealth))
                if p.currHealth <= 0 or p.flee:
                    if p.flee == True:
                        print("You flee combat")
                        break
                    else:
                        print("You have died")
                        break
                elif m.currHealth <= 0:
                    print("The Monster is has fainted")
                    p.Inv += m.loot[:]
                    print(p.Inv)
                    break
                else:
                    pass
        p.currHealth = p.maxHP

    def flee(self):
        global p
        p.flee = True

    def combat_turn(self, t):
        if t.entType == 'mob':
            i = str(1) #random.randint(1, 2)
        else:
            print('-'*16)
            print('1: ' + 'Use a skill', '2: ' + 'Equip an item', '3: ' + 'Flee', sep='\n')
            i = input("It's your turn! What would you like to do?")
        if i == '1':
            Skills.use_skill(Skills, t)
        elif i == '2':
            self.get_equipment(self)
        elif i == '3':
            self.flee(self)
            return
        else:
            print('Please input a valid id number.')
            self.combat_turn(self, t)
            return

    def monster_gen(self):
        global m
        name = self.mnl[random.randint(0, len(self.mnl)-1)]
        hp = random.randint(1, p.stats['Level'] + 1) * 10
        m = self.Monster(name, hp, currHealth=m.maxHP, dmg=2, entType='mob', speed=1)
        # Buffing from Player Challenge Rating
        m.level = p.level
        m.dmg += m.level
        m.dr = 1
        m.skills = [Skills.BasicAtk, Skills.Stab]
        x = 0
        tl = []
        while x <= (m.level // 2):
            r = random.randint(0, len(Items.itemlist))
            tl = Items.itemlist[r:r+1]
            x += 1
        m.loot = tl

    def show_stats(self, t):
        print("-" * 16)
        # t is the targeted object
        if t.entType == "player":
            print(t.name + "'s" + " Stats")
            for a, b in p.stats.items():
                print(str(a), end=': ' + str(b) + '\n')

        elif t.entType == 'mob':
            print(t.name + "'s" + " Stats")
            for a, b in t.__dict__.items():
                if a == 'loot':
                    continue
                elif a == 'entType':
                    continue
                elif a == 'skills':
                    print(a.capitalize() + ':')
                    for c in b:
                        print('|' + str(b[b.index(c)].name) + '|')
                    break
                print(a.capitalize() + ':', str(b))
        print("-" * 16)



    def get_equipment(self):
        print(p.Inv)
        #get equipment in Inventory
        for b in p.Inv[1:]:
            print(p.Inv.index(b), p.Inv[p.Inv.index(b)].name)
        e = input("Input the number id of what you would like to equip?")
        try:
            e = int(e)
        except ValueError:
            print("please enter a whole number")
            self.get_equipment(self)
            return
        else:
            pass
        #Equip the item
        try:
            p.Inv[0].insert(int(e)-1, p.Inv[int(e)])
            p.Inv.append(p.Inv[int(e)])
            del p.Inv[int(e)]
        except IndexError:
            print("Choose a valid id")
            self.get_equipment(self)
            return
        print(p.Inv)

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
        def __init__(self, name, maxHP, currHealth, dmg, entType, speed):
            self.name = name
            self.maxHP = maxHP
            self.currHealth = currHealth
            self.dmg = dmg
            self.loot = []
            self.level = self.maxHP + self.dmg
            self.entType = entType
            self.speed = speed
        skills = []

    # Start game
    def setup_game(self):
        self.game_start(Game)


#calculates the dmg of the skill used
def damage_calc(s, t):
    global m
    global p
    if t.entType == 'player':
        m.currHealth -= (p.dmg - m.dr)
        print(p.name + " used " + s.name)
    else:
        p.currHealth -= (m.dmg - p.dr)
        print((m.name + " used " + s.name))


class Skills:
    def use_skill(self, t):
        sl = t.skills
        us = []
        for a in sl:
            if a.useable:
                us.append(a)
                continue
        if t.entType == 'mob':
            s = int(random.randint(0, len(sl)-1))
            us[s].dc(us[s], t)
            return
        else:
            pass
        for b in us:
            print(us.index(b)+1, b.name)
            continue
        print("What skill would you like to use?")
        s = int(input()) - 1
        us[s].dc(us[s], t)

    class Stab:
        name = "Stab"
        useable = True
        dc = damage_calc

    class BasicAtk:
        name = 'Basic Attack'
        useable = True
        dc = damage_calc




    #New player
def new_player():
    global p
    #Clear everything
    p = Player('', '', '', 0, 0, 0, 0, 0, 0, 0, 'player', 1)
    p.Equ = []
    p.Inv = []
    p.stats = {}
    #Start Character creation
    player_creator()


def new_mob():
    global m
    #Clear everything
    m = Game.Monster('', '', '', '', 'mob', 1)
    m.Equ = []
    m.Inv = []
    m.skills = []
    m.stats = {}
    #Start Character creation
    Game.monster_gen(Game)


if __name__ == '__main__':
    new_player()
    Game.show_stats(Game, p)
    new_mob()
    Game.game_start(Game)




#try this structure for Skills/Monster


class Color:

    # constructor method
    def __init__(self):
        # object attributes
        self.name = 'Green'
        self.lg = self.Lightgreen()

    def show(self):
        print("Name:", self.name)

    # create Lightgreen class
    class Lightgreen:
        def __init__(self):
            self.name = 'Light Green'
            self.code = '024avc'

        def display(self):
            print("Name:", self.name)
            print("Code:", self.code)


# create Color class object
outer = Color()

# method calling
outer.show()

# create a Lightgreen
# inner class object
g = outer.lg

# inner class method calling
g.display()


