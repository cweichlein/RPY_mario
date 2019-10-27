import pygame, sys
from pygame.time import *
<<<<<<< Updated upstream
from block import brick,bricks
# from pygame.sprite import Group
=======
from block import brick,bricks, pipe, invincible_block, floor_blocks, question, bridge, cliff, mushroom_block, liquid, boss_bridge
# from pygame.sprite import Group
from pygame.locals import Color
>>>>>>> Stashed changes
from pygame.math import Vector2
from settings import Settings
from level_1_4 import level_1_4


<<<<<<< Updated upstream


def main():
=======
class main:
>>>>>>> Stashed changes
    """Initializes the game and runs the game loop"""
    def __init__(self):
        pygame.init()

        self.disp = pygame.display.set_mode((496,496))

        self.settings = Settings()
        self.myBrick1 = bricks(self.settings, Vector2(0, 0), Vector2(10, 1), self.disp, 'blue')
        self.myBrick2 = bricks(self.settings, Vector2(0, 1), Vector2(1, 10), self.disp, 'grey')
        self.myBrick3 = bricks(self.settings, Vector2(22, 1), Vector2(5, 5), self.disp, 'gold')
        self.Pipe_top = pipe(self.settings, Vector2(1, 1), Vector2(2, 15), self.disp, True, True, False)
        self.pipe_bot = pipe(self.settings, Vector2(3, 1), Vector2(2, 15), self.disp, True, False, False)
        self.pipe_left = pipe(self.settings, Vector2(5, 1), Vector2(15, 2), self.disp, False, False, False)
        self.pipe_right = pipe(self.settings, Vector2(5, 3), Vector2(15, 2), self.disp, False, False, True)
        self.invinc_block1 = invincible_block(self.settings, Vector2(30, 30), self.disp)
        self.invinc_block2 = invincible_block(self.settings, Vector2(30, 29), self.disp)
        self.floor1 = floor_blocks(self.settings, Vector2(0, 29), 30, self.disp, True)
        self.floor2 = floor_blocks(self.settings, Vector2(0, 30), 30, self.disp, True)
        self.question1 = question(self.settings,Vector2(5, 24), self.disp)
        self.question2 = question(self.settings, Vector2(10, 24), self.disp)
        self.question3 = question(self.settings, Vector2(15, 24), self.disp)
        self.bridge1 = bridge(self.settings,Vector2(6, 24), 3, self.disp)
        self.cliff1 = cliff(self.settings, Vector2(15,15), Vector2(4, 20), self.disp)
        self.mush1 = mushroom_block(self.settings, Vector2(5, 15), Vector2(5, 20), self.disp, True)
        self.mush2 = mushroom_block(self.settings, Vector2(7, 21), Vector2(7, 15), self.disp, False)
        self.liquid1 = liquid(self.settings, Vector2(22, 22), Vector2(8,10),self.disp, True)
        self.liquid2 = liquid(self.settings, Vector2(2, 22), Vector2(8, 10), self.disp, False)
        self.boss_bridge1 = boss_bridge(self.settings, Vector2(6, 27), 10, self.disp)

        self.level_1_4 = level_1_4(self.settings,self.disp)

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def test_scroll(self):
        self.cliff1.move()
        self.mush1.move()
        self.mush2.move()
        self.myBrick1.move()
        self.myBrick2.move()
        self.Pipe_top.move()
        self.pipe_bot.move()
        self.pipe_left.move()
        self.pipe_right.move()
        self.invinc_block1.move()
        self.invinc_block2.move()
        self.floor1.move()
        self.floor2.move()
        self.question1.move()
        self.question2.move()
        self.question3.move()
        self.bridge1.move()
        self.liquid1.move()
        self.liquid2.move()
        self.myBrick3.move()
        self.boss_bridge1.move()

    def test_assets(self):
        self.disp.fill(Color('#00ffff'))
        self.cliff1.draw()
        self.mush1.draw()
        self.mush2.draw()
        self.liquid1.draw()
        self.liquid2.draw()
        self.myBrick1.draw()
        self.myBrick2.draw()
        self.myBrick3.draw()
        self.Pipe_top.draw()
        self.pipe_bot.draw()
        self.pipe_left.draw()
        self.pipe_right.draw()
        self.invinc_block1.draw()
        self.invinc_block2.draw()
        self.floor1.draw()
        self.floor2.draw()
        self.question1.draw()
        self.question2.draw()
        self.question3.draw()
        self.bridge1.draw()
        self.boss_bridge1.draw()

<<<<<<< Updated upstream
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
=======
    def run_game(self):
        while True: # main game loop
            self.check_event()
>>>>>>> Stashed changes

            self.level_1_4.draw()
            self.level_1_4.move()
            # self.scroll()


            pygame.display.update()
            pygame.time.wait(1)


if __name__ == '__main__':
    M = main()
    M.run_game()