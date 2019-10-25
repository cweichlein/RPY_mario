import pygame, sys
from pygame.time import *
from block import brick,bricks
# from pygame.sprite import Group
from pygame.math import Vector2
from settings import Settings




def main():
    """Initializes the game and runs the game loop"""
    pygame.init()

    disp = pygame.display.set_mode((500,500))

    settings = Settings()
    myBrick1 = bricks(settings,Vector2(0,0),10, True)
    myBrick2 = bricks(settings, Vector2(0, 16), 10, False)

    def check_event():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def run_game():
        while True: # main game loop
            check_event()
            myBrick1.draw()
            myBrick2.draw()

            disp.update()
            time.sleep(0.1)





if __name__ == '__main__':
    M = main()
    M.run_game()