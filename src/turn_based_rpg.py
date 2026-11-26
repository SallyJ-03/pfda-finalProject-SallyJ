import sys


import pygame


from button import Button
from battle import Battle
from text_particle import Text_Particle
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


def draw_text(text, x, y, surface, scale=1):
    font = pygame.font.SysFont('arialblack', int(30*scale))
    TEXT_COL = (0, 0, 0)

    img = font.render(text, True, TEXT_COL)
    surface.blit(img, (x, y))


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Turn-based RPG")

    player = entity.Player()
    stage = 4
    battle = Battle(player, stage)
    screen_state = 'GAME'

    battle_background = pygame.image.load('ui_img/battle_bkground_temp.png').convert_alpha()
    menu_background = pygame.image.load('ui_img/menu_bkground_temp.png').convert_alpha()

    fight_button_img = pygame.image.load('ui_img/fight_button_temp.png').convert_alpha()
    fight_button = Button(10, 474, fight_button_img,scale=1)
    heavy_button_img = pygame.image.load('ui_img/heavy_att_button_temp.png').convert_alpha()
    heavy_button = Button(10, 597, heavy_button_img, scale=1)
    item_button_img = pygame.image.load('ui_img/item_button_temp.png').convert_alpha()
    item_button = Button(561, 474, item_button_img,scale=1)
    menu_button_img = pygame.image.load('ui_img/menu_button_temp.png').convert_alpha()
    menu_button = Button(561, 597, menu_button_img, scale=1)

    retry_button_img = pygame.image.load('ui_img/retry_button_temp.png').convert_alpha()
    retry_button = Button(300, 300, retry_button_img,scale=1)

    resume_button_img = pygame.image.load('ui_img/resume_button_temp.png').convert_alpha()
    resume_button = Button(100, 100, resume_button_img, scale=1)
    quit_button_img = pygame.image.load('ui_img/quit_button_temp.png').convert_alpha()
    quit_button = Button(100, 500, quit_button_img, scale=1)

    player_hp_bar = Health_Bar(10, 10, 450, 50, player.max_health)
    enemy_hp_bar = Health_Bar(620, 10, 450, 50, battle.enemy.max_health)

    text_particles = Text_Particle()

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and battle.dodge_timer.active:
                    battle.in_action = False
                    battle.dodge_timer.deactivate()
                    text_particles.add("DODGED", 'PLAYER')

        text_particles.update(dt)

        screen.fill((200, 200, 255))

        if screen_state == 'GAME':

            screen.blit(battle_background)

            battle.dodge_timer.update()
            player.update(battle.player)
            player_hp_bar.update(screen, player.health)
            enemy_hp_bar.update(screen, battle.enemy.health)

            draw_text(f"items left: {player.item_count}", 0, 365, screen)
            draw_text(f"stage {stage}", 475, 10, screen)

            if player.health <= 0:
                screen_state = 'GAME_OVER'
                battle.in_action = False
            elif battle.enemy.health <= 0:
                stage += 1
                if stage > 4:
                    screen_state = 'GAME_WIN'
                else:
                    battle = Battle(player, stage)
                    enemy_hp_bar.max_hp = battle.enemy.max_health
                battle.in_action = False

            elif battle.dodge_timer.active:
                # dodge animation
                pass

            elif battle.in_action:
                if battle.turn_count == 0:
                    battle.execute_turn('PLAYER')
                    location = 'ENEMY'
                    if player.move == 2:
                        location = 'PLAYER'
                    text_particles.add(battle.damage, location, player.move)
                elif battle.turn_count == 1:
                    battle.start_dodge_timer()
                else:
                    battle.execute_turn('ENEMY')
                    text_particles.add(battle.damage, 'PLAYER', battle.enemy.move)

            elif fight_button.draw(screen):
                battle.set_up_turns(player_move=0)
            elif heavy_button.draw(screen):
                battle.set_up_turns(player_move=1)
            elif item_button.draw(screen):
                battle.set_up_turns(player_move=2)
                if player.item_count <= 0:
                    print("no more items")
                    battle.in_action = False
            elif menu_button.draw(screen):
                screen_state = 'MENU'

        elif screen_state == 'GAME_OVER':
            if retry_button.draw(screen):
                player = entity.Player()
                stage = 0
                battle = Battle(player, stage)
                screen_state = 'GAME'

        elif screen_state == 'GAME_WIN':
            screen.fill(pygame.Color(200, 200, 255))
            draw_text("YOU WIN", 300, 200, screen, 3)
            if retry_button.draw(screen):
                player = entity.Player()
                stage = 0
                battle = Battle(player, stage)
                screen_state = 'GAME'                

        elif screen_state == 'MENU':
            screen.blit(menu_background)

            if resume_button.draw(screen):
                screen_state = 'GAME'
            elif quit_button.draw(screen):
                pygame.quit()
                sys.exit()


        text_particles.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)


if __name__ == "__main__":
    main()