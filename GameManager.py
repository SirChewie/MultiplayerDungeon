def get_players_info():
    from main import pls
    gcr = 0
    for x in pls:
        print("Player: " + x.name, "\nLevel: " + x.level, "\nClass: " + x.cl)
        gcr += x.level
    return gcr


class Game:

    def __init__(self, floor, deaths, kills):
        self.kills = kills
        self.deaths = deaths
        self.floor = floor


class Monster:
    def __init__(self):
        self.health = 10
        self.dmg = 2
        self. loot = []
        self.level = self.health + self.dmg


def game_start():
    g = Game(1, 0, 0)
    get_players_info()
    print("Floor: " + str(g.floor))
    print("Game start")
    encounter()


def encounter():
    monster_gen()


def monster_gen():
    global m
    m = Monster()
    #Player Callenge Rating
    m.health *= get_players_info()
    m.dmg += get_players_info()

    for a in m.__dict__.keys():
        print(a)
