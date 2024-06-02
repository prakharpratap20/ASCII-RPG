import random
from utils import clear, draw, save, load
from battle import battle
from shop import shop
from mayor import mayor
from cave import cave
from data import map, biom


class Game:
    def __init__(self):
        self.run = True
        self.menu = True
        self.play = False
        self.rules = False
        self.key = False
        self.fight = False
        self.standing = True
        self.buy = False
        self.speak = False
        self.boss = False

        self.HP = 50
        self.HPMAX = 50
        self.ATK = 3
        self.pot = 1
        self.elix = 0
        self.gold = 0
        self.x = 0
        self.y = 0
        self.name = ""

        self.y_len = len(map) - 1
        self.x_len = len(map[0]) - 1

    def run(self):
        while self.run:
            while self.menu:
                self.show_menu()
            while self.play:
                save(self)  # autosave
                clear()
                if not self.standing:
                    if biom[map[self.y][self.x]]["e"]:
                        if random.randint(0, 100) < 30:
                            self.fight = True
                            battle(self)

                if self.play:
                    self.show_game_status()
                    self.handle_input()

    def show_menu(self):
        print("1, NEW GAME")
        print("2, LOAD GAME")
        print("3, RULES")
        print("4, QUIT GAME")

        if self.rules:
            print("I'm the creator of this game and these are the rules.")
            self.rules = False
            input("> ")
        else:
            choice = input("# ")

        if choice == "1":
            clear()
            self.name = input("# What's your name, hero? ")
            self.menu = False
            self.play = True
        elif choice == "2":
            if load(self):
                self.menu = False
                self.play = True
        elif choice == "3":
            self.rules = True
        elif choice == "4":
            self.run = False

    def show_game_status(self):
        draw()
        print(f"LOCATION: {biom[map[self.y][self.x]]['t']}")
        draw()
        print(f"NAME: {self.name}")
        print(f"HP: {self.HP}/{self.HPMAX}")
        print(f"ATK: {self.ATK}")
        print(f"POTIONS: {self.pot}")
        print(f"ELIXIRS: {self.elix}")
        print(f"GOLD: {self.gold}")
        print(f"COORD: {self.x}, {self.y}")
        draw()
        print("0 - SAVE AND QUIT")
        if self.y > 0:
            print("1 - NORTH")
        if self.x < self.x_len:
            print("2 - EAST")
        if self.y < self.y_len:
            print("3 - SOUTH")
        if self.x > 0:
            print("4 - WEST")
        if self.pot > 0:
            print("5 - USE POTION (30HP)")
        if self.elix > 0:
            print("6 - USE ELIXIR (50HP)")
        if map[self.y][self.x] in ["shop", "mayor", "cave"]:
            print("7 - ENTER")
        draw()

    def handle_input(self):
        dest = input("# ")

        if dest == "0":
            self.play = False
            self.menu = True
            save(self)
        elif dest == "1" and self.y > 0:
            self.y -= 1
            self.standing = False
        elif dest == "2" and self.x < self.x_len:
            self.x += 1
            self.standing = False
        elif dest == "3" and self.y < self.y_len:
            self.y += 1
            self.standing = False
        elif dest == "4" and self.x > 0:
            self.x -= 1
            self.standing = False
        elif dest == "5" and self.pot > 0:
            self.pot -= 1
            self.heal(30)
        elif dest == "6" and self.elix > 0:
            self.elix -= 1
            self.heal(50)
        elif dest == "7":
            if map[self.y][self.x] == "shop":
                self.buy = True
                shop(self)
            elif map[self.y][self.x] == "mayor":
                self.speak = True
                mayor(self)
            elif map[self.y][self.x] == "cave":
                self.boss = True
                cave(self)
        else:
            self.standing = True

    def heal(self, amount):
        self.HP = min(self.HP + amount, self.HPMAX)
        print(f"{self.name}'s HP refilled to {self.HP}!")
