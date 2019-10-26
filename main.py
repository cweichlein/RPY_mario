import pygame, sys
from pygame.time import *
from pygame.math import Vector2

from block import brick,bricks, pipe
from settings import Settings
from mario import Mario


class main:
    """Initializes the game and runs the game loop"""
    def __init__(self):
        pygame.init()

        self.disp = pygame.display.set_mode((1000,1000))

        self.settings = Settings()
        self.myBrick1 = bricks(self.settings, Vector2(0, 0), 10, self.disp, True)
        self.myBrick2 = bricks(self.settings, Vector2(0, 1), 10, self.disp, False)
        self.Pipe_top = pipe(self.settings, Vector2(1, 1), Vector2(2, 15), self.disp, True, True, False)
        self.pipe_bot = pipe(self.settings, Vector2(3, 1), Vector2(2, 15), self.disp, True, False, False)
        self.mario = Mario(screen=self.disp, settings=self.settings)

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def run_game(self):
        while True: # main game loop
            self.disp.fill((0, 255, 255))
            self.check_event()
            self.myBrick1.draw()
            self.myBrick2.draw()
            self.Pipe_top.draw()
            self.pipe_bot.draw()
            self.mario.update()

            self.mario.blitme()

            pygame.display.flip()
            pygame.time.wait(1)


if __name__ == '__main__':
    M = main()
    M.run_game()