from utils import clear, draw


def mayor(game):
    while game.speak:
        clear()
        draw()
        print(f"Hello there, {game.name}!")
        if game.ATK < 10:
            print(
                "You're not strong enough to face the dragon yet! Keep practicing and come back later!")
            game.key = False
        else:
            print(
                "You might want to take on the dragon now! Take this key but be careful with the beast!")
            game.key = True
        draw()
        print("1 - LEAVE")
        draw()

        choice = input("# ")

        if choice == "1":
            game.speak = False
