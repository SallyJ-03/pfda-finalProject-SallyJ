import sys


import pygame
import random


from timer import Timer
from button import Button


WIDTH = 1080
HEIGHT = 720


class Entity:

    def __init__(self, health, attack, defense, speed):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.move = 0
        self.name = 'ENTITY'


class Player(Entity):
    def __init__(self, health=100, attack=25, defense=25, speed=50):
        super().__init__(health, attack, defense, speed)
        self.name = 'PLAYER'


class Enemy(Entity):

    def __init__(self, health=50, attack=15, defense=15, speed=50, difficulty=0):
        super().__init__(health, attack, defense, speed)
        self.difficulty = difficulty
        self.name = 'ENEMY'


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


def sort_speed(player: Player, enemy: Enemy):
    order = ()
    if player.speed > enemy.speed:
        order = (player, enemy)
    elif enemy.speed > player.speed:
        order = (enemy, player)
    else:
        if random.randint(0,1) == 0:
            order = (player, enemy)
        else:
            order = (enemy, player)
    return order


def calculate_damage(attack: int, defense: int, move: int):
    move_damage = 50.0
    if move == 1:
        move_damage = 70.0
    
    dmg = int((2.0 * (float(attack) / float(defense)) * move_damage) / 10)
    if dmg <= 0:
        dmg = 1
    
    return dmg


def execute_turn(user: Entity, target: Entity, move: int):
    if user.name == 'ENEMY':
        dodge_timer = Timer(1000,autostart=True)
    target.health -= calculate_damage(user.attack, target.defense, move)


def battle(player: Player, enemy: Enemy):
    print(f"Player health: {player.health}")
    print(f"Enemy health: {enemy.health}")

    player.move = 0
    enemy.move = choose_enemy_move(enemy.difficulty)
    first, second = sort_speed(player, enemy)
    execute_turn(first, second, first.move)
    if second.health <= 0:
        return
    execute_turn(second, first, second.move)
    if first.health <= 0:
        return



def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Turn-based RPG")

    player = Player()
    stage = 0
    enemy = Enemy(difficulty=stage)
    
    fight_img = pygame.image.load('ui_img/fight_button_temp.png').convert_alpha()
    fight_button = Button(100, 100, fight_img)
    retry_img = pygame.image.load('ui_img/retry_button_temp.png').convert_alpha()
    retry_button = Button(300, 300, retry_img)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((200, 200, 255))

        if player.health <= 0:
            retry_button.draw(screen)

        elif fight_button.draw(screen):
            battle(player, enemy)
        
        if enemy.health <= 0:
            print("increase difficulty")
            stage += 1
            enemy = Enemy(difficulty=stage)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()