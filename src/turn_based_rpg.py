import sys


import pygame
import random


WIDTH = 1080
HEIGHT = 720


class Button():

    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        # get mouse position
        mouse_pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                print('CLICKED')
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))


class Entity():

    def __init__(self, health, attack, defense, speed):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.move = 0


class Player(Entity):
    def __init__(self, health=100, attack=25, defense=25, speed=50):
            super().__init__(health, attack, defense, speed)


class Enemy(Entity):

    def __init__(self, health=50, attack=15, defense=15, speed=50, difficulty=0):
        super().__init__(health, attack, defense, speed)
        self.difficulty = difficulty


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
    target.health -= calculate_damage(user.attack, target.defense, move)


def battle(player):
    enemy = Enemy()

    while player.health > 0 and enemy.health > 0:
        print(f"Player health: {player.health}")
        print(f"Enemy health: {enemy.health}")
        # ask for player input
        player.move = int(input("choose move: [0] Attack, [1] Str Attack"))
        # calculate enemy move
        enemy.move = choose_enemy_move(enemy.difficulty)
        # determine who goes first
        first, second = sort_speed(player, enemy)
        # execute turn
        execute_turn(first, second, first.move)
        execute_turn(second, first, second.move)

        # increase battle_num if a side is dead
        # switch turn and execute turn
        # increase battle_num if a side is dead


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Turn-based RPG")

    player = Player(health=100, attack=25, defense=25, speed=50)
    fight_img = pygame.image.load('ui_img/fight_button_temp.png').convert_alpha()
    fight_button = Button(100, 100, fight_img)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        fight_button.draw(screen)

        #battle(player)    

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()