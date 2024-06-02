from utils import clear, draw
from battle import battle


def cave(game):
    while game.boss:
        clear()
        draw()
        print("Here lies the cave of the dragon. What will you do?")
        draw()
        if game.key:
            print("1 - USE KEY")
        print("2 - TURN BACK")
        draw()

        choice = input("# ")

        if choice == "1" and game.key:
            game.fight = True
            battle(game)
        elif choice == "2":
            game.boss = False
