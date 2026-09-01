import random

class Adventurer:
    """Represent the user in our game"""
    def __init__(self, name: str) -> None:
        self.name = name
        self.strength: int = random.randint(3, 18)
        self.constitution: int = random.randint(3, 18)
        self.hit_points: int =self.constitution + random.randint(1, 8)

        # tha bag start at empty
        self.bag: list[Item] = []


# now lets create he Item class
class Item:
    """An item which can be held by adventurer """
    def __init__(self, name: str, min_damage: int, max_damage: int) -> None:
        if name != None:
            self.name: str = name
        else:
            self.name: str = "Unknown Item"
        self.min_damage: int = min_damage
        self.max_damage: int = max_damage

class Monster:
    def __init__(self, name: str, min_dmg: int, max_dmg: int, hit_points: int) -> None:
        self.name = name
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.hit_points = hit_points

    def create_monster(self): # class function to create random monster
        monsters = ['Ghost', 'Goblin', 'Python']

        # Now we need to choose a monster
        name = random.choice(monsters)

        if name == 'Ghost':
            return Monster(name, random.randint(0, 1), random.randint(1, 2), 2)
        elif name == 'Goblin':
            return Monster(name, random.randint(0, 1), random.randint(1, 2), 10)
        elif name == 'Python':
            return Monster(name, random.randint(3, 6), random.randint(6, 12), 5)

# now let's create an object of adventurer
adventurer = Adventurer("Abdulbaset")
