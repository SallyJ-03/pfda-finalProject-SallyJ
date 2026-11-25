import pygame


class Text:

    def __init__(self, text="", pos=(), color=pygame.Color(255, 255, 255)):
        self.text = text
        self.pos = pos
        self.life = 500
        self.age = 0
        self.dead = False
        self.alpha = 255
        self.color = color

    def draw(self, surface):
        if self.dead:
            return
        
        font = pygame.font.SysFont('arialblack', 30)
        TEXT_COL = (0, 0, 0)

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

    def add(self, text, pos=(), color=pygame.Color(255, 255, 255)):
        text = str(text)
        if text == '-1':
            text = ''
        particle = Text(text, pos, color)
        self.particles.insert(0, particle)

    def draw(self, surface):
        for particle in self.particles:
            particle.draw(surface)
