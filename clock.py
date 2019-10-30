from pygame.time import get_ticks

class clock:
    def __init__(self):
        self.cur_time = self.prev_time = get_ticks()
        self.delt_time = 0

    def delta_time(self):
        self.prev_time = self.cur_time
        self.cur_time = get_ticks()
        self.delt_time = (self.cur_time - self.prev_time)
