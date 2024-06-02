import random
from utils import clear, draw
from data import mobs, e_list


def battle(game):
    enemy = "Dragon" if game.boss else random.choice(e_list)
    hp = mobs[enemy]["hp"]
    hpmax = hp
    atk = mobs[enemy]["at"]
    g = mobs[enemy]["go"]

    while game.fight:
        clear()
        draw()
        print(f"Defeat the {enemy}!")
        draw()
        print(f"{enemy}'s HP: {hp}/{hpmax}")
        print(f"{game.name}'s HP: {game.HP}/{game.HPMAX}")
        print(f"POTIONS: {game.pot}")
        print(f"ELIXIRS: {game.elix}")
        draw()
        print("1 - ATTACK")
        if game.pot > 0:
            print("2 - USE POTION (30HP)")
        if game.elix > 0:
            print("3 - USE ELIXIR (50HP)")
        draw()

        choice = input("# ")

        if choice == "1":
            hp -= game.ATK
            print(f"{game.name} dealt {game.ATK} damage to the {enemy}.")
            if hp > 0:
                game.HP -= atk
                print(f"{enemy} dealt {atk} damage to {game.name}.")
            input("> ")

        elif choice == "2" and game.pot > 0:
            game.pot -= 1
            game.heal(30)
            game.HP -= atk
            print(f"{enemy} dealt {atk} damage to {game.name}.")
            input("> ")

        elif choice == "3" and game.elix > 0:
            game.elix -= 1
            game.heal(50)
            game.HP -= atk
            print(f"{enemy} dealt {atk} damage to {game.name}.")
            input("> ")

        if game.HP <= 0:
            print(f"{enemy} defeated {game.name}...")
            draw()
            game.fight = False
            game.play = False
            game.run = False
            print("GAME OVER")
            input("> ")

        if hp <= 0:
            print(f"{game.name} defeated the {enemy}!")
            draw()
            game.fight = False
            game.gold += g
            print(f"You've found {g} gold!")
            if random.randint(0, 100) < 30:
                game.pot += 1
                print("You've found a potion!")
            if enemy == "Dragon":
                draw()
                print("Congratulations, you've finished the game!")
                game.boss = False
                game.play = False
                game.run = False
            input("> ")
            clear()
