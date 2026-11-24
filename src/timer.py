from pygame.time import get_ticks

class Timer:

    def __init__(self, duration):
        self.duration = duration
        self.start_time = 0
        self.active = False

    # activate function
    def activate(self):
        self.active = True
        self.start_time = get_ticks()

    # deactivate function

    # update function