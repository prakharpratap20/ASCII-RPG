map = [
    ["plains", "plains", "plains", "plains", "forest", "mountain", "cave"],
    ["forest", "forest", "forest", "forest", "forest", "hills", "mountain"],
    ["forest", "fields", "bridge", "plains", "hills", "forest", "hills"],
    ["plains", "shop", "town", "mayor", "plains", "hills", "mountain"],
    ["plains", "fields", "fields", "plains", "hills", "mountain", "mountain"]
]

biom = {
    "plains": {"t": "PLAINS", "e": True},
    "forest": {"t": "WOODS", "e": True},
    "fields": {"t": "FIELDS", "e": False},
    "bridge": {"t": "BRIDGE", "e": True},
    "town": {"t": "TOWN CENTRE", "e": False},
    "shop": {"t": "SHOP", "e": False},
    "mayor": {"t": "MAYOR", "e": False},
    "cave": {"t": "CAVE", "e": False},
    "mountain": {"t": "MOUNTAIN", "e": True},
    "hills": {"t": "HILLS", "e": True}
}

e_list = ["Goblin", "Orc", "Slime"]

mobs = {
    "Goblin": {"hp": 15, "at": 3, "go": 8},
    "Orc": {"hp": 35, "at": 5, "go": 18},
    "Slime": {"hp": 30, "at": 2, "go": 12},
    "Dragon": {"hp": 100, "at": 8, "go": 100}
}
