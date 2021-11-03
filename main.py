

#Player Object Template
class Player:
    def __init__(self,  name, sex, cl, level):
        self.name = name
        self. sex = sex
        self.cl = cl
        self.level = level

    #Player creeation
    def player_creator(self):
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
#New player
def new_player():
    Player.player_creator(Player)


#Start game
def setup_game():
    Game.game_start(Game)





if __name__ == '__main__':
    from GameManager import Game
    new_player()
    setup_game()
    print(Player)


