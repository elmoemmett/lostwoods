'''
Lost Woods Game - Classes Module
Emmett Tomkinson
Feb 24, 2023
'''

class Enemy:
    '''
    The Enemy class is used for the enemies encountered in the game
    Each enemy has a different power based on the weapon used against it
    '''
    def __init__(self, name, bow_hp, sword_hp, damage, rarity, total_hp) -> None:
        self.name = name
        self.bow_hp = bow_hp
        self.sword_hp = sword_hp
        self.damage = damage
        self.rarity = rarity
        self.total_hp = total_hp

bokoblin = Enemy("Bokoblin", bow_hp = 60, sword_hp = 30, damage = 5, rarity = 1, total_hp = 60)
moblin = Enemy("Moblin", bow_hp = 70, sword_hp = 50, damage = 10, rarity = 2, total_hp = 70)
lynel = Enemy("Lynel", bow_hp = 60, sword_hp = 80, damage = 15, rarity = 3, total_hp = 80)
ganon = Enemy("Ganon", bow_hp = 100, sword_hp= 100, damage = 25, rarity = None, total_hp = 150)

class Weapon:
    '''
    The weapon class is used to store the sword and bow objects
    Each of these objects has different actions and short names which are used in print statements
    '''
    def __init__(self, name, short_name, action, power) -> None:
        self.name = name
        self.action = action
        self.power = power
        self.short_name = short_name

sword = Weapon(name = "Sword and Shield", short_name = "sword", action = "swing", power = 10)
bow = Weapon(name = "Bow and Arrow", short_name = "arrow", action = "release", power = 10)

class Prize:
    '''
    The prize class is used to define the objects that are contained in chests in the game
    '''
    def __init__(self, name, rarity) -> None:
        self.name = name
        self.rarity = rarity

heart = Prize(name = "Heart", rarity = 1)
potion = Prize(name = "Potion", rarity = 2)
clue = Prize(name = "clue", rarity = 3)

class Player:
    '''
    The player class was important to maintain the player's HP throughout the game
    As a future improvment, I will move the has_potion variable to be an argument in this
    '''
    def __init__(self, link_hp: int) -> None:
        self.link_hp = link_hp
