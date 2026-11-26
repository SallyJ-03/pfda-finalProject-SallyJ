class Entity:

    def __init__(self, max_health, attack, defense):
        self.max_health = max_health
        self.health = max_health
        self.attack = attack
        self.defense = defense
        self.move = 0
        self.name = 'ENTITY'


class Player(Entity):
    def __init__(self, max_health=100, attack=25, defense=25):
        super().__init__(max_health, attack, defense)
        self.name = 'PLAYER'
        self.item_count = 5

    def update(self, new_stats: Player):
        self.health = new_stats.health
        self.item_count = new_stats.item_count
        self.move = new_stats.move


class Enemy(Entity):

    def __init__(self, max_health=50, attack=15, defense=15, difficulty=0):
        super().__init__(max_health, attack, defense)
        self.difficulty = difficulty
        self.name = 'ENEMY'
