from utils import clear, draw


def shop(game):
    while game.buy:
        clear()
        draw()
        print("Welcome to the shop!")
        draw()
        print(f"GOLD: {game.gold}")
        print(f"POTIONS: {game.pot}")
        print(f"ELIXIRS: {game.elix}")
        print(f"ATK: {game.ATK}")
        draw()
        print("1 - BUY POTION (30HP) - 5 GOLD")
        print("2 - BUY ELIXIR (MAXHP) - 8 GOLD")
        print("3 - UPGRADE WEAPON (+2ATK) - 10 GOLD")
        print("4 - LEAVE")
        draw()

        choice = input("# ")

        if choice == "1":
            if game.gold >= 5:
                game.pot += 1
                game.gold -= 5
                print("You've bought a potion!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "2":
            if game.gold >= 8:
                game.elix += 1
                game.gold -= 8
                print("You've bought an elixir!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "3":
            if game.gold >= 10:
                game.ATK += 2
                game.gold -= 10
                print("You've upgraded your weapon!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "4":
            game.buy = False
