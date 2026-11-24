import sys


import pygame


WIDTH = 1080
HEIGHT = 720


class Entity():

    def __init__(self, health, attack, defense, speed):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed


class Player(Entity):
    def __init__(self, health=100, attack=25, defense=25, speed=50):
            super().__init__(health, attack, defense, speed)


class Enemy(Entity):

    def __init__(self, health=50, attack=15, defense=15, speed=50, difficulty=0):
        super().__init__(health, attack, defense, speed)
        self.difficulty = difficulty

def choose_enemy_move():
    return 1


def battle(player):
    enemy = Enemy()

    while player.health > 0 and enemy.health > 0:
        print(f"Player health: {player.health}")
        print(f"Enemy health: {enemy.health}")
        # ask for player input
        player_move = input("fight:\n")
        # calculate enemy move
        enemy_move = choose_enemy_move()
        # determine who goes first
        # execute turn
        enemy.health -= 10
        player.health -= 10

        # increase battle_num if a side is dead
        # switch turn and execute turn
        # increase battle_num if a side is dead


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Turn-based RPG")

    player = Player(health=100, attack=25, defense=25, speed=50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        battle(player)    

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()