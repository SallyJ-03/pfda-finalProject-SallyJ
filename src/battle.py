import random
import entity


from timer import Timer


class Battle:

    def __init__(self, player: entity.Player, stage):
        self.enemy = entity.Enemy(difficulty=stage)
        self.player = player
        self.turn_count = 0
        self.dodge_timer = Timer(500)
        self.in_action = False


    def __choose_enemy_move__(self, diff: int):
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

    def __calculate_damage__(self, attack: int, defense: int, move: int):
        move_damage = 50.0
        if move == 1:
            move_damage = 70.0
        
        dmg = int((2.0 * (float(attack) / float(defense)) * move_damage) / 10)
        if dmg <= 0:
            dmg = 1
        
        return dmg

    def use_item(self):
        if self.player.item_count > 0:
            self.player.health += 20
            self.player.item_count -= 1
        else:
            print("no more items left!")

        if self.player.health > self.player.max_health:
            self.player.health = self.player.max_health

    def start_dodge_timer(self):
        self.dodge_timer.activate()
        self.turn_count = 2

    def set_up_turns(self, player_move):
        self.player.move = player_move
        self.enemy.move = self.__choose_enemy_move__(self.enemy.difficulty)
        self.turn_count = 0
        self.in_action = True

    def execute_turn(self, turn):
        dmg = 0
        if turn == 'PLAYER':
            self.turn_count = 1
            if self.player.move == 2:
                self.use_item()
            else:
                dmg = self.__calculate_damage__(self.player.attack, self.enemy.defense, 0)
                self.enemy.health -= dmg
        elif turn == 'ENEMY':
            self.turn_count = 0
            dmg = self.__calculate_damage__(self.enemy.attack, self.player.defense, self.enemy.move)
            self.player.health -= dmg
            self.in_action = False
