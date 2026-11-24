import random
import entity


def choose_enemy_move(diff: int):
    move_chance = random.randint(1,100)
    move = 0
    if diff == 0:
        move = random.randint(0,1)
    elif diff == 1:
        if move_chance < 70:
            move = 1
    elif diff == 2:
        if move_chance < 80:
            move = 1
    elif diff == 3:
        if move_chance < 90:
            move = 1
    else:
        move = 1
    return move


def calculate_damage(attack: int, defense: int, move: int):
    move_damage = 50.0
    if move == 1:
        move_damage = 70.0
    
    dmg = int((2.0 * (float(attack) / float(defense)) * move_damage) / 10)
    if dmg <= 0:
        dmg = 1
    
    return dmg


def execute_turn(user: entity.Entity, target: entity.Entity, move):
    dmg = calculate_damage(user.attack, target.defense, move)
    return target.health - dmg
