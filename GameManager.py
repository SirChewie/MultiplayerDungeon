
class Game:

    def __init__(self, floor, deaths, kills):
        self.kills = kills
        self.deaths = deaths
        self.floor = floor
    pls = []
    gcr = 0

    def get_players_info(self):
        for x in self.pls:
            print(x.name)
            self.gcr += x.level

    def game_start(self):
        g = Game(1, 0, 0)
        self.get_players_info(Game)
        print("Floor: " + str(g.floor))
        print("Game start")
        self.encounter(Game)

    def encounter(self):
        self.Monster.monster_gen(Game)

    class Monster:
        def __init__(self):
            self.health = 10
            self.dmg = 2
            self. loot = []
            self.level = self.health + self.dmg

        def monster_gen(self):
            global m
            m = Game.Monster()
            #Buffing from Player Callenge Rating
            m.health *= Game.gcr
            m.dmg += Game.gcr

            for a in m.__dict__.items():
                if a == ('loot', []):
                    continue
                print(a)

