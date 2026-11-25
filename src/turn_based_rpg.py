import sys


import pygame


from button import Button
from battle import Battle
import entity


WIDTH = 1080
HEIGHT = 720


class Health_Bar:

    def __init__(self, x, y, w, h, max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp

    def draw(self, surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, color='red', rect=(self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, color='green', rect=(self.x, self.y, self.w * ratio, self.h))

    def update(self, surface, new_hp):
        self.hp = new_hp
        self.draw(surface)


def draw_text(text, x, y, surface):
    font = pygame.font.SysFont('arialblack', 30)
    TEXT_COL = (0, 0, 0)

    img = font.render(text, True, TEXT_COL)
    surface.blit(img, (x, y))
    pass


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Turn-based RPG")

    player = entity.Player()
    stage = 0
    battle = Battle(player, stage)

    fight_button_img = pygame.image.load('ui_img/fight_button_temp.png').convert_alpha()
    fight_button = Button(100, 100, fight_button_img)
    item_button_img = pygame.image.load('ui_img/item_button_temp.png').convert_alpha()
    item_button = Button(600, 100, item_button_img)
    retry_button_img = pygame.image.load('ui_img/retry_button_temp.png').convert_alpha()
    retry_button = Button(300, 300, retry_button_img)

    player_hp_bar = Health_Bar(100, 500, 300, 40, player.max_health)
    enemy_hp_bar = Health_Bar(500, 500, 300, 40, battle.enemy.max_health)

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and battle.dodge_timer.active:
                    battle.in_action = False
                    battle.dodge_timer.deactivate()
                    print("DODGED")

        battle.dodge_timer.update()

        screen.fill((200, 200, 255))
        player.update(battle.player.health, battle.player.item_count)
        player_hp_bar.update(screen, player.health)
        enemy_hp_bar.update(screen, battle.enemy.health)

        draw_text(f"items left: {player.item_count}", 0, 0, screen)

        if player.health <= 0:
            retry_button.draw(screen)

        elif battle.enemy.health <= 0:
            stage += 1
            if stage > 4:
                print("you win")
            else:
                print(f"stage {stage}")
                battle = Battle(player, stage)
            battle.in_action = False

        elif battle.dodge_timer.active:
            # dodge animation
            pass

        elif battle.in_action:
            print(battle.in_action)
            if battle.turn_count == 0:
                battle.execute_turn('PLAYER')
            elif battle.turn_count == 1:
                battle.start_dodge_timer()
            else:
                battle.execute_turn('ENEMY')
                player.update(battle.player.health, battle.player.item_count)

        elif fight_button.draw(screen):
            battle.set_up_turns(player_move=0)

        elif item_button.draw(screen):
            battle.set_up_turns(player_move=2)


        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()