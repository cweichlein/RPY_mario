import pygame, sys
from pygame.time import *
<<<<<<< Updated upstream
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

=======
from mario import Mario
from timer import Timer
from clock import clock
from block import brick,bricks, pipe, invincible_block, floor_blocks, question, bridge, cliff, mushroom_block, liquid, boss_bridge, plant, flag, vine, coin
# from pygame.sprite import Group
from pygame.locals import Color
from pygame.math import Vector2
from settings import Settings
from level_1_4 import level_1_4
from pygame.sprite import *
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
        self.Pipe_top = pipe(self.settings, Vector2(1, 1), Vector2(2, 15), self.disp, True, True, False)
        self.pipe_bot = pipe(self.settings, Vector2(3, 1), Vector2(2, 15), self.disp, True, False, False)
        self.pipe_left = pipe(self.settings, Vector2(5, 1), Vector2(15, 2), self.disp, False, False, False)
=======
        self.myBrick4 = bricks(self.settings, Vector2(6, 8), Vector2(5, 1), self.disp, 'cloud')
        self.myBrick5 = bricks(self.settings, Vector2(22, 23), Vector2(2, 2), self.disp, 'coral')
        self.Pipe_top = pipe(self.settings, Vector2(1, 1), Vector2(2, 15), self.disp, True, True, False)
        self.pipe_bot = pipe(self.settings, Vector2(3, 1), Vector2(2, 15), self.disp, True, False, False)
        self.pipe_left = pipe(self.settings, Vector2(4, 1), Vector2(15, 2), self.disp, False, False, False)
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream

        self.level_1_4 = level_1_4(self.settings,self.disp)
=======
        self.plant1 = plant(self.settings, Vector2(2, 27), self.disp, 'smll_tree')
        self.plant2 = plant(self.settings, Vector2(3, 26), self.disp, 'tall_tree')
        self.plant3 = plant(self.settings, Vector2(4, 28), self.disp, 'smll_hedge')
        self.plant4 = plant(self.settings, Vector2(5, 27), self.disp, 'tall_hedge')
        self.plant5 = plant(self.settings, Vector2(6, 28), self.disp, 'bush')
        self.flag1 = flag(self.settings, Vector2(28, 20), self.disp)
        self.coin1 = coin(self.settings, Vector2(15, 14),self.disp, 'reg')
        self.coin2 = coin(self.settings, Vector2(16, 14), self.disp, 'wat')
        self.coin3 = coin(self.settings, Vector2(17, 14), self.disp, 'cav')
        self.vine1 = vine(self.settings, Vector2(15, 16), Vector2(4, 4), self.disp, 'blue', True)
        self.vine2 = vine(self.settings, Vector2(20, 25), Vector2(4, 4), self.disp, 'green', False)

        self.my_mario = Mario(settings=self.settings, screen=self.disp)

        self.cur_level = level_1_4(self.settings,self.disp)
        self.delta1 = clock()
>>>>>>> Stashed changes

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

<<<<<<< Updated upstream
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
=======
    def test_scroll(self, delta):
        self.cliff1.move(delta)
        self.mush1.move(delta)
        self.mush2.move(delta)
        self.myBrick1.move(delta)
        self.myBrick2.move(delta)
        self.Pipe_top.move(delta)
        self.pipe_bot.move(delta)
        self.pipe_left.move(delta)
        self.pipe_right.move(delta)
        self.invinc_block1.move(delta)
        self.invinc_block2.move(delta)
        self.floor1.move(delta)
        self.floor2.move(delta)
        self.question1.move(delta)
        self.question2.move(delta)
        self.question3.move(delta)
        self.bridge1.move(delta)
        self.liquid1.move(delta)
        self.liquid2.move(delta)
        self.myBrick3.move(delta)
        self.boss_bridge1.move(delta)
        self.plant1.move(delta)
        self.plant2.move(delta)
        self.plant3.move(delta)
        self.plant4.move(delta)
        self.plant5.move(delta)
        self.flag1.move(delta)
        self.coin1.move(delta)
        self.coin2.move(delta)
        self.vine2.move(delta)
        self.coin3.move(delta)
        self.vine1.move(delta)
        self.myBrick4.move(delta)
        self.myBrick5.move(delta)

        # self.my_mario.update(delta)
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
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


=======
        self.plant1.draw()
        self.plant2.draw()
        self.plant3.draw()
        self.plant4.draw()
        self.plant5.draw()
        self.flag1.draw()
        self.coin1.draw()
        self.coin2.draw()
        self.vine2.draw()
        self.coin3.draw()
        self.vine1.draw()
        self.boss_bridge1.draw()
        self.myBrick4.draw()
        self.myBrick5.draw()

    def game_func(self):
        pass

    def run_game(self):
        while True:  # main game loop
            self.delta1.delta_time()
            # print(self.delta1.delt_time)
            self.check_event()

            # todo mario.move(x)
            # self.cur_level.move()  # todo pass in distance mario moves
            # self.cur_level.draw()  # draw everything to the screen
            self.test_scroll(self.delta1.delt_time)

            self.test_assets()
            # todo swap levels
            # if level over destroy cur level and create next level
>>>>>>> Stashed changes
            pygame.display.update()
            pygame.time.wait(1)


if __name__ == '__main__':
    M = main()
    M.run_game()