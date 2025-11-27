import random

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    @staticmethod
    def ability():
        rolls = [random.randint(1,6) for _ in range(5)]
        rolls.remove(min(rolls))
        rolls.remove(max(rolls))
        return sum(rolls)


def modifier(value):
    match value:
        case 3:
            return -4
        case 4 | 5:
            return -3
        case 6 | 7:
            return -2
        case 8 | 9:
            return -1
        case 10 | 11:
            return 0
        case 12 | 13:
            return 1
        case 14 | 15:
            return 2
        case 16 | 17:
            return 3
        case 18:
            return 4
        
