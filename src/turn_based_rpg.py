import sys


import pygame


from button import Button
from timer import Timer
import battle
import entity


WIDTH = 1080
HEIGHT = 720


# health bar class
# init
# draw
# calculate ratio
# draw two rects on top of each other


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Turn-based RPG")

    fight_button_img = pygame.image.load('ui_img/fight_button_temp.png').convert_alpha()
    fight_button = Button(100, 100, fight_button_img)
    item_button_img = pygame.image.load('ui_img/item_button_temp.png').convert_alpha()
    item_button = Button(600, 100, item_button_img)
    retry_button_img = pygame.image.load('ui_img/retry_button_temp.png').convert_alpha()
    retry_button = Button(300, 300, retry_button_img)

    player = entity.Player()
    stage = 0
    enemy = entity.Enemy(difficulty=stage)
    in_action = False
    turn_count = 0
    dodge_timer = Timer(1000)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and dodge_timer.active:
                    in_action = False
                    dodge_timer.deactivate()
                    print("DODGED")

        dodge_timer.update()

        screen.fill((200, 200, 255))


        if player.health <= 0:
            retry_button.draw(screen)

        elif enemy.health <= 0:
            stage += 1
            if stage > 4:
                print("you win")
            else:
                print("increase difficulty")
                enemy = entity.Enemy(difficulty=stage)

        elif dodge_timer.active:
            pass

        elif in_action:
            if turn_count == 0:
                enemy.update_health(battle.execute_turn(player, enemy, player.move))
                turn_count += 1
            elif turn_count == 1:
                dodge_timer.activate()
                print("timer")
                turn_count += 1
            else:
                player.update_health(battle.execute_turn(enemy, player, enemy.move))
                in_action = False
                turn_count = 0

        elif fight_button.draw(screen):
            print(f"Player health: {player.health}")
            print(f"Enemy health: {enemy.health}")
            player.move = 0
            enemy.move = battle.choose_enemy_move(enemy.difficulty)
            in_action = True
            turn_count = 0

        elif item_button.draw(screen):
            player.item_count -= 1
            player.update_health(player.health + 20)
            if player.health > 100:
                player.update_health(100)
            enemy.move = battle.choose_enemy_move(enemy.difficulty)
            in_action = True
            turn_count = 0


        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()