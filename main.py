#Player Object Templete
class Player:
    def __init__(self,  name, sex, cl, level):
        self.name = name
        self. sex = sex
        self.cl = cl
        self.level = 1


#Player creeation
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


#New player
def new_player():
    global p1
    player_creator()
    p1 = Player
    pls[str(p1.name)] = p1


#Start game
def setup_game():
    from GameManager import game_start
    game_start()

#Empty player object
p1 = None

#Players Dict
pls = {}

if __name__ == '__main__':
    new_player()
    setup_game()


