import sys


import pygame


WIDTH = 1080
HEIGHT = 720


class Player():

    def __init__(self, health=100, attack=25, defense=25, speed=50):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed


class Enemy():

    def __init__(self, health=10, attack=10, defense=10, speed=10):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed


def choose_enemy_move():
    return 1


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Turn-based RPG")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        battle_num = 1
        while battle_num == 1:
            # ask for player input
            player_move = int(input("Choose your move: [1] Attack"))
            # calculate enemy move
            enemy_move = choose_enemy_move()
            # determine who goes first
            # execute turn
            # increase battle_num if a side is dead
            # switch turn and execute turn
            # increase battle_num if a side is dead

            battle_num += 1

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()