import random
import entity


from timer import Timer


class Battle:

    def __init__(self, player: entity.Player, stage):
        match stage:
            case 0:
                self.enemy = entity.Enemy()
            case 1:
                self.enemy = entity.Enemy(max_health=75, attack=20, defense=20, difficulty=stage)
            case 2:
                self.enemy = entity.Enemy(max_health=100, attack=25, defense=25, difficulty=stage)
            case 3:
                self.enemy = entity.Enemy(max_health=130, attack=30, defense=30, difficulty=stage)
            case 4:
                self.enemy = entity.Enemy(max_health=150, attack=35, defense=35, difficulty=stage)
        self.player = player
        self.turn_count = 0
        self.dodge_timer = Timer(500)
        self.in_action = False

        self.damage = 0


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
        if turn == 'PLAYER':
            self.turn_count = 1
            if self.player.move == 2:
                self.use_item()
                self.damage = -1
            else:
                self.damage = self.__calculate_damage__(self.player.attack, self.enemy.defense, self.player.move)
                self.enemy.health -= self.damage

        elif turn == 'ENEMY':
            self.turn_count = 0
            self.damage = self.__calculate_damage__(self.enemy.attack, self.player.defense, self.enemy.move)
            self.player.health -= self.damage
            self.in_action = False
