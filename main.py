import pygame, sys, random
from pygame.locals import *
from pygame.time import *
from mario import Mario
from timer import Timer
from clock import clock
from block import brick,bricks, pipe, invincible_block, floor_blocks, question, bridge, cliff, mushroom_block, liquid, boss_bridge, plant, flag, vine, coin
# from pygame.sprite import Group
from pygame.locals import Color
from pygame.math import Vector2
from settings import Settings
from level_1_4 import level_1_4
from level_1_1 import level_1_1
from pygame.sprite import *
from dave_mario import mario

class main:
    """Initializes the game and runs the game loop"""
    def __init__(self):
        pygame.init()

        self.disp = pygame.display.set_mode((496, 256))

        self.settings = Settings()
        '''
        self.myBrick1 = bricks(self.settings, Vector2(0, 0), Vector2(10, 1), self.disp, 'blue')
        self.myBrick2 = bricks(self.settings, Vector2(0, 1), Vector2(1, 10), self.disp, 'grey')
        self.myBrick3 = bricks(self.settings, Vector2(22, 1), Vector2(5, 5), self.disp, 'gold')
        self.myBrick4 = bricks(self.settings, Vector2(6, 8), Vector2(5, 1), self.disp, 'cloud')
        self.myBrick5 = bricks(self.settings, Vector2(22, 23), Vector2(2, 2), self.disp, 'coral')
        self.Pipe_top = pipe(self.settings, Vector2(1, 1), Vector2(2, 15), self.disp, True, True, False)
        self.pipe_bot = pipe(self.settings, Vector2(3, 1), Vector2(2, 15), self.disp, True, False, False)
        self.pipe_left = pipe(self.settings, Vector2(4, 1), Vector2(15, 2), self.disp, False, False, False)
        self.pipe_right = pipe(self.settings, Vector2(5, 3), Vector2(15, 2), self.disp, False, False, True)
        self.invinc_block1 = invincible_block(self.settings, Vector2(30, 30), self.disp)
        self.invinc_block2 = invincible_block(self.settings, Vector2(30, 29), self.disp)
        self.floor1 = floor_blocks(self.settings, Vector2(0, 29), Vector2(30,2), self.disp)
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
        '''

        self.pipe_left = pipe(self.settings, Vector2(4, 1), Vector2(15, 2), self.disp, False, False, False)
        self.mario1 = mario(Vector2(128, 128), self.disp)

        #self.my_mario = Mario(settings=self.settings, screen=self.disp)

        self.cur_level = level_1_1(self.settings, self.disp)
        # print(self.cur_level.get_rect())

        self.delta1 = clock()

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                # Change the keyboard variables.
                if event.key == K_LEFT or event.key == K_a:
                    self.mario1.move_right = False
                    self.mario1.move_left = True
                if event.key == K_RIGHT or event.key == K_d:
                    self.mario1.move_right = True
                    self.mario1.move_left = False
                if event.key == K_UP or event.key == K_w:
                    self.mario1.move_down = False
                    if not self.mario1.jump:
                        self.mario1.jump = True
                if event.key == K_DOWN or event.key == K_s:
                    self.mario1.move_down = True
                    self.mario1.jump = False
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_LEFT or event.key == K_a:
                    self.mario1.move_left = False
                if event.key == K_RIGHT or event.key == K_d:
                    self.mario1.move_right = False
                if event.key == K_UP or event.key == K_w:
                    self.mario1.jump = False
                if event.key == K_DOWN or event.key == K_s:
                    self.mario1.move_down = False

    def test_scroll(self, velocity, delta):
        self.cliff1.move(velocity, delta)
        self.mush1.move(velocity, delta)
        self.mush2.move(velocity, delta)
        self.myBrick1.move(velocity, delta)
        self.myBrick2.move(velocity, delta)
        self.Pipe_top.move(velocity, delta)
        self.pipe_bot.move(velocity, delta)
        self.pipe_left.move(velocity, delta)
        self.pipe_right.move(velocity, delta)
        self.invinc_block1.move(velocity, delta)
        self.invinc_block2.move(velocity, delta)
        self.floor1.move(velocity, delta)
        self.question1.move(velocity, delta)
        self.question2.move(velocity, delta)
        self.question3.move(velocity, delta)
        self.bridge1.move(velocity, delta)
        self.liquid1.move(velocity, delta)
        self.liquid2.move(velocity, delta)
        self.myBrick3.move(velocity, delta)
        self.boss_bridge1.move(velocity, delta)
        self.plant1.move(velocity, delta)
        self.plant2.move(velocity, delta)
        self.plant3.move(velocity, delta)
        self.plant4.move(velocity, delta)
        self.plant5.move(velocity, delta)
        self.flag1.move(velocity, delta)
        self.coin1.move(velocity, delta)
        self.coin2.move(velocity, delta)
        self.vine2.move(velocity, delta)
        self.coin3.move(velocity, delta)
        self.vine1.move(velocity, delta)
        self.myBrick4.move(velocity, delta)
        self.myBrick5.move(velocity, delta)

        # self.my_mario.update(velocity, delta)

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
        self.question1.draw()
        self.question2.draw()
        self.question3.draw()
        self.bridge1.draw()
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
            x = self.cur_level.get_rect()
            self.mario1.move(delta=self.delta1.delt_time, rect_list=x)
            self.mario1.draw()
            #self.pipe_left.draw()
            #self.pipe_left.move(-self.mario1.movement, self.delta1.delt_time)
            # todo mario.move(x)
            if self.mario1.pos.x > 249 and self.mario1.velocity.x > 0:
                self.cur_level.move(-self.mario1.movement, self.delta1.delt_time / 2)  # todo pass in distance mario moves
            self.cur_level.draw()  # draw everything to the screen
            # self.test_scroll(-self.mario1.movement, self.delta1.delt_time)

            # self.test_assets()
            self.mario1.draw()
            # todo swap levels
            # if level over destroy cur level and create next level
            pygame.display.update()
            # pygame.time.wait(1)


if __name__ == '__main__':
    M = main()
    M.run_game()