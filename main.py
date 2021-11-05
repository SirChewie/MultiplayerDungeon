# Player creation
def player_creator():
    name = input("What is your name?:\n")
    if 2 < len(name) > 16:
        print("Naming Rules:\n1: Less than 16 characters and more than 2.")
        return
    Player.name = str(name)
    sex = input("Pick a sex:\n"
                "M: Male\n" 
                "F: Female\n"
                )
    sex = str(sex.upper())
    if sex == "F" or "M":
        if sex == "F":
            sex = "Female"
        else:
            sex = "Male"
        Player.sex = str(sex)
    else:
        print("Please enter a correct sex 'M' or 'F'")
        print(sex.upper())
        return
    Player.cl = "Villager"
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
            m = Game.Monster()
            #Buffing from Player Callenge Rating
            m.health *= Game.gcr
            m.dmg += Game.gcr

            for a in m.__dict__.items():
                if a == ('loot', []):
                    continue
                print(a)

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
        print(p)


