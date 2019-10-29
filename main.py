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
        self.blocks = []
        self.myBrick1 = bricks(self.settings, Vector2(0, 0), 10, self.disp, True)
        self.myBrick2 = bricks(self.settings, Vector2(0, 1), 10, self.disp, False)
        self.Pipe_top = pipe(self.settings, Vector2(1, 1), Vector2(2, 15), self.disp, True, True, False)
        self.pipe_bot = pipe(self.settings, Vector2(3, 1), Vector2(2, 15), self.disp, True, False, False)
        self.blocks.append(self.myBrick1)
        self.blocks.append(self.myBrick2)
        self.blocks.append(self.Pipe_top)
        self.blocks.append(self.pipe_bot)
        self.mario = Mario(screen=self.disp, settings=self.settings, blocks=self.blocks)

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

            pygame.display.flip()


if __name__ == '__main__':
    M = main()
    M.run_game()