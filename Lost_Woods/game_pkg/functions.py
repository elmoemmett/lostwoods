'''
Lost Woods Game - Functions Module
Emmett Tomkinson
Feb 24, 2023
Credit for the Triforce print at the end of this file goes to
https://stackoverflow.com/questions/69517111/need-to-print-triforce-using-recursion
'''

import time
import random
from game_pkg.classes import *
path = ["start", "left", "right", "right", "forward", "left", "forward", "forward", "right", "left", "boss", "final"]
rarity_list = [1, 1, 1, 1, 2, 2, 2, 3]
player = Player(100)
PATH_IDX = 0
NUM_POTIONS = 0
def encounter():
    '''
    Function to be called when the player encounters an enemy
    '''
    enemy_rarity = random.choice(rarity_list)
    if enemy_rarity == 1:
        enemy = bokoblin
    elif enemy_rarity == 2:
        enemy = moblin
    else:
        enemy = lynel

    print(f"You've encountered a {enemy.name}!")
    time.sleep(1)
    while True:
        option1 = input("Choose your weapon!\nType 'sword' for Sword and Shield or 'bow' for Bow and Arrow\n").lower()
        time.sleep(1)
        if option1 == "sword":
            weapon = sword
            print("You chose the Sword and Shield!")
            break
        elif option1 == "bow":
            weapon = bow
            print("You chose the Bow and Arrow")
            break
        else:
            print("Please enter sword or bow")

    print("Link HP: ", int(player.link_hp))

    option = input("Type A to attack or P to drink potion\n").lower()
    if option == "p":
        drink_potion()
        battle(enemy, weapon)
    else:
        battle(enemy, weapon)
    return

def battle(enemy, weapon):
    '''
    Function to go through the battle sequence
    '''
    if weapon == sword:
        enemy_hp = enemy.sword_hp
    else:
        enemy_hp = enemy.bow_hp

    while player.link_hp > 0:
        random_float = random.random()
        print("You", weapon.action, "your", weapon.short_name)
        player.link_hp = player.link_hp - (enemy.damage * random_float)
        enemy_hp = enemy_hp - (weapon.power * random_float)
        print("Link HP:",int(player.link_hp))
        print(enemy.name, "HP:", int(enemy_hp))
        if player.link_hp <= 1:
            game_over_option = input("Game Over. Try again? yes/no")
            if game_over_option == "yes":
                player.link_hp = 100
                break
            elif game_over_option == "no":
                print("Thank you for playing!")
                exit()
            else:
                print("Please type yes or no")
        elif enemy_hp <= 1:
            print("You won the battle!")
            move_rooms()
            break
        battle_action = input("Type A to attack or P to drink potion\n").lower()
        if battle_action == "p":
            drink_potion()

def start():
    '''
    Function to start the game and go through the opening sequence
    '''
    print("In the dark woods of Hyrule, link enters a forest.")
    time.sleep(2)
    print("He sees three possible paths ahead ... Left, Right, or Forward.")
    time.sleep(2)

def move_rooms():
    '''
    Function used to ask the player which direciton they want to go and determine if they choose the correct path
    If they choose the correct path, they are moved to the next index and the prize() function is called
    If they choose the incorrect path, they enounter an enemy with the encounter() funciton
    If the next room is the boss room, the boss_fight() function is called
    '''
    global PATH_IDX
    if path[PATH_IDX + 1] == "boss":
        boss_fight()
    move = input("To continue with the adventure, type left, right, or forward. To quit, type quit.\n").lower()
    time.sleep(1)
    if move in path:
        if move == path[PATH_IDX + 1]:
            PATH_IDX += 1
            chest()
        elif move == "quit":
            exit()
        else:
            encounter()
    else:
        print("Please type left, right, or forward.")

def drink_potion():
    '''
    Function used to drink a potion and restore health to 100
    As potions are used, the number is decreased
    '''
    global NUM_POTIONS
    if NUM_POTIONS > 0 :
        potion_value = 100 - player.link_hp
        player.link_hp = player.link_hp + potion_value
        NUM_POTIONS -= 1
        time.sleep(1)
        print("You drink your potion and your health is back to", int(player.link_hp))
        time.sleep(1)
        print("You attack!")
        time.sleep(1)
    else:
        print("Sorry, you don't have any potion")

def chest():
    '''
    Function that is called when the player chooses the correct path.
    One of three random prizes are presented
    '''
    prize = heart
    prize_rarity = random.choice(rarity_list)
    if prize_rarity == 1:
        prize = heart
    elif prize_rarity == 2:
        prize = potion
    elif prize_rarity == 3:
        prize = clue
    print(f"You found a chest! Inside the chest is a {prize.name}!\n")
    if prize == heart:
        player.link_hp = player.link_hp + 25
        print("Your HP has been increased to", int(player.link_hp), "\n")
        time.sleep(1)
    elif prize == potion:
        global NUM_POTIONS
        NUM_POTIONS += 1
        print("This potion will restore your health to 100 when you use it.\n")
    elif prize == clue:
        if path[PATH_IDX + 1] == "left":
            print("The clue says: 'Keep going! You've got nothing left to lose!'\n")
        elif path[PATH_IDX + 1] == "right":
            print("The clue says: 'Make sure you choose the right way!'\n")
        elif path[PATH_IDX + 1] == "forward":
            print("The clue says: 'Victory is straight ahead!'\n")

def boss_fight():
    '''
    Function that is called for the final boss fight.
    The final boss (Ganon) is an object of the Enemy class, but his attack sequence varies.
    Because of this, the battle actions are included in this code, with the twist that Ganon
    can change positions throughout the battle. The player is given the option to choose 
    their weapon. The weapon's effectiveness varies based on Ganon's position (on the ground vs.
    in the air).
    Once Ganon is defeated, the final closing sequence is called
    '''
    weapon = sword
    print("You come to a clearing and find a chest. Inside the chest is a potion!\n")
    time.sleep(1)
    global NUM_POTIONS
    NUM_POTIONS += 1
    enemy = ganon
    ganon_hp = enemy.total_hp
    has_fairy = True
    print("This potion will restore your health to 100 when you use it.\n")
    time.sleep(4)
    print("You hear a laugh in the darkness ...")
    time.sleep(2)
    print("'You .... I have been waiting for this day for ages ...'")
    time.sleep(2)
    print("'You're much smaller than I pictured you ...'")
    time.sleep(2)
    print("'All these years, I have waited for the 'chosen one' ...'")
    time.sleep(2)
    print("'... seeing you now, I am certain that victory is in my grasp!'")
    time.sleep(1)

    while player.link_hp > 0:
        random_float = random.random()
        ganon_status_list = ["stands on the ground", "flies in the air"]
        ganon_status = random.choice(ganon_status_list)
        print("Ganon", ganon_status, ". Choose your weapon")
        ganon_weapon = input("Type 'sword' for Sword and Shield or 'bow' for Bow and Arrow\n").lower()
        time.sleep(1)
        if ganon_weapon == "sword":
            weapon = sword
        elif ganon_weapon == "bow":
            weapon = bow
        else:
            print("Please enter sword or bow")

        if ganon_status == "stands on the ground":
            sword.power = 15
            bow.power = 5
        else:
            sword.power = 5
            bow.power = 15
        print("You", weapon.action, "your", weapon.short_name)
        player.link_hp = int(player.link_hp - (enemy.damage * random_float))
        ganon_hp = ganon_hp - (weapon.power * random_float)
        print("Link HP:",int(player.link_hp))
        print(enemy.name, "HP:", int(ganon_hp))
        if player.link_hp <= 1:
            if has_fairy is True:
                print("You fall to the ground ... then suddenly, a fairy appears!")
                print("Your HP has been restored to 100!")
                fairy_value = 100 - player.link_hp
                player.link_hp = player.link_hp + fairy_value
                has_fairy = False
            else:
                game_over_option = input("Game Over. Try again? yes/no\n").lower()
                if  game_over_option == "yes":
                    player.link_hp = 100
                    ganon_hp = 150
                    boss_fight()
                elif game_over_option == "no":
                    print("Thank you for playing!")
                    exit()
                else:
                    print("Please type yes or no")
        elif ganon_hp <= 1:
            time.sleep(2)
            print("Ganon falls to the ground")
            time.sleep(3)
            print("'Noooooooo! This simply is not possible!'")
            time.sleep(3)
            print("'How could a young thing such as you defeat me!")
            time.sleep(3)
            print("'I am ageless. You have won this battle, but I have only just begun ...'")
            time.sleep(3)
            print("Ganon's body slowly evaporates before your eyes ... and he is gone")
            time.sleep(4)
            print("You see a light ahead, and a forest clearing")
            time.sleep(3)
            print("'Link ... once more, you have defeated the darkness'")
            time.sleep(3)
            print("'Your efforts have not been in vain'")
            time.sleep(3)
            print("'Take this ... and carry it to a far away land, where it can be sealed away safely'")
            time.sleep(3)
            print("'Always remember ... you are and always will be the chosen one. Thank you, Link.")
            time.sleep(4)
            print_triforce(10)
            time.sleep(3)
            print("The End")
            exit()
        battle_action = input("Type A to attack or P to drink potion\n").lower()
        if battle_action == "p":
            drink_potion()

#Below is the code for the Triforce symbol at the end of the game
#I do not take credit for this code

def space_f(space):
    '''
    space function
    '''
    if space == 0:
        return
    print(" ", end = "")
    space_f(space - 1)

def triangle(n):
    '''
    Triange function
    '''
    if n == 0:
        return
    return '* '*n
    triangle(n - 1)

def top_triangle(n, count, base):
    '''
    top triange function
    '''
    if n == 0:
        return
    space_f(base)
    print(triangle(count - n + 1))
    return top_triangle(n - 1, count, base-1)

def bottom_triangles(n, count, base):
    '''
    bottom triange function
    '''
    if n == 0:
        return
    space_f(n-1)
    print(triangle(count - n + 1), end="")
    space_f(n-1)
    space_f(n-1)
    print(triangle(count - n + 1))
    return bottom_triangles(n - 1, count, base-1)


def print_triforce(n):
    '''
    print whole triforce
    '''
    if n == 0:
        print(" ")
    height = 2 * n
    base = height - 1
    top_triangle(n, n, base)
    bottom_triangles(n, n, base)
