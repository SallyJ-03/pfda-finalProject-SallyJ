class Entity:

    def __init__(self, health, attack, defense):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.move = 0
        self.name = 'ENTITY'

    def update_health(self, new_health):
        self.health = new_health


class Player(Entity):
    def __init__(self, health=100, attack=25, defense=25):
        super().__init__(health, attack, defense)
        self.name = 'PLAYER'


class Enemy(Entity):

    def __init__(self, health=50, attack=15, defense=15, difficulty=0):
        super().__init__(health, attack, defense)
        self.difficulty = difficulty
        self.name = 'ENEMY'
