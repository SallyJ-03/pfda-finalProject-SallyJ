import pygame


class Text:

    def __init__(self, text="", pos='', type=0):
        self.text = text
        self.pos = self._set_pos_(pos)
        self.life = 500
        self.age = 0
        self.dead = False
        self.alpha = 255
        self.color = self._set_color_(type)

    def _set_color_(self, type):
        color = pygame.Color(255, 255, 255)
        if type == 1:
            color = pygame.Color(255, 255, 0)
        if type == 2:
            color = pygame.Color(0, 255, 0)

        return color

    def _set_pos_(self, location):
        pos = ()
        if location == 'PLAYER':
            pos = (200, 300)
        elif location == 'ENEMY':
            pos = (800, 300)

        return pos

    def draw(self, surface):
        if self.dead:
            return
        
        font = pygame.font.SysFont('arialblack', 30)
        TEXT_COL = self.color

        img = font.render(self.text, True, TEXT_COL)
        img.set_alpha(self.alpha)
        surface.blit(img, self.pos)

    def update(self, dt):
        self.age += dt
        self._update_pos()
        if self.age > self.life:
            self.dead = True
        self.alpha = 255 * (1 - self.age / self.life)

    def _update_pos(self):
        x, y = self.pos
        y -= 1
        self.pos = (x, y)


class Text_Particle:

    def __init__(self):
        self.particles = []

    def update(self, dt):
        for idx, particle in enumerate(self.particles):
            particle.update(dt)
            if particle.dead:
                del self.particles[idx]

    def add(self, text, pos='', type=0):
        text = str(text)
        particle = Text(text, pos, type)
        self.particles.insert(0, particle)

    def draw(self, surface):
        for particle in self.particles:
            particle.draw(surface)
