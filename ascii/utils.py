import os


def clear():
    os.system("clear")


def draw():
    print("xX--------------------xX")


def save(game):
    save_data = [
        game.name, str(game.HP), str(game.ATK), str(game.pot), str(game.elix), str(
            game.gold), str(game.x), str(game.y), str(int(game.key))
    ]
    with open("load.txt", "w") as file:
        for item in save_data:
            file.write(item + "\n")


def load(game):
    try:
        with open("load.txt", "r") as file:
            load_list = file.readlines()
            if len(load_list) == 9:
                game.name = load_list[0].strip()
                game.HP = int(load_list[1].strip())
                game.ATK = int(load_list[2].strip())
                game.pot = int(load_list[3].strip())
                game.elix = int(load_list[4].strip())
                game.gold = int(load_list[5].strip())
                game.x = int(load_list[6].strip())
                game.y = int(load_list[7].strip())
                game.key = bool(int(load_list[8].strip()))
                clear()
                print(f"Welcome back, {game.name}!")
                input("> ")
                return True
            else:
                print("Corrupt save file!")
                input("> ")
    except OSError:
        print("No loadable save file!")
        input("> ")
    return False
