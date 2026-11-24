from pygame.time import get_ticks

class Timer:

    def __init__(self, duration, autostart=False):
        self.duration = duration
        self.start_time = 0
        self.active = False
        if autostart:
            self.activate()

    # activate function
    def activate(self):
        self.active = True
        self.start_time = get_ticks()

    # deactivate function
    def deactivate(self):
        self.active = False
        self.start_time = 0

    # update function
    def update(self):
        if self.active:
            current_time = get_ticks()
            if current_time - self.start_time >= self.duration:
                self.deactivate()