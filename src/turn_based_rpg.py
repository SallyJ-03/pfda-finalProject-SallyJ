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

    def __init__(self, health=50, attack=15, defense=15, speed=50, difficulty=1):
        super().__init__(health, attack, defense, speed)
        self.difficulty = difficulty

def choose_enemy_move():
    return 1


def battle():
    battle_num = 1
    while battle_num == 1:
        enemy = Enemy(health=30, attack=10, defense=10, speed=50, difficulty=1)
        # ask for player input
        player_move = int(input("Choose your move: [1] Attack\n"))
        # calculate enemy move
        enemy_move = choose_enemy_move()
        # determine who goes first
        # execute turn
            

        # increase battle_num if a side is dead
        # switch turn and execute turn
        # increase battle_num if a side is dead

        battle_num += 1


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

        battle()    

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()