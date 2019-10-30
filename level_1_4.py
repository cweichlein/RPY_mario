from block import *
from settings import Settings
from game_functions import create_block

class level_1_4:
    def __init__(self, setting: Settings, disp: display):
        self.disp = disp

        self.super_list = list()

        self.bricks = list()
        self.bricks.append(bricks(setting, Vector2(0, 0), Vector2(128, 1), disp, 'grey'))
        self.bricks.append(bricks(setting, Vector2(0, 1), Vector2(20, 2), disp, 'grey'))
        self.bricks.append(bricks(setting, Vector2(0, 5), Vector2(3, 7), disp, 'grey'))
        self.bricks.append(bricks(setting, Vector2(3, 6), Vector2(1, 6), disp, 'grey'))
        self.bricks.append(bricks(setting, Vector2(4, 7), Vector2(1, 5), disp, 'grey'))
        self.bricks.append(bricks(setting, Vector2(5, 8), Vector2(6, 4), disp, 'grey'))
        self.lavas = list()
        self.lavas.append(liquid(setting, Vector2(11, 10), Vector2(1, 2), disp, False))
        self.lavas.append(liquid(setting, Vector2(22, 11), Vector2(3, 1), disp, False))
        self.lavas.append(liquid(setting, Vector2(28, 11), Vector2(3, 1), disp, False))
        self.bricks.append(bricks(setting, Vector2(12, 8), Vector2(10, 4), disp, 'grey'))
        self.bricks.append(bricks(setting, Vector2(25, 8), Vector2(3, 4), disp, 'grey'))
        self.bricks.append(bricks(setting, Vector2(31, 7), Vector2(25, 5), disp, 'grey'))
        self.bricks.append(bricks(setting, Vector2(33, 1), Vector2(23, 3), disp, 'grey'))
        self.bricks.append(bricks(setting, Vector2(56, 8), Vector2(26, 4), disp, 'grey'))
        self.bricks.append(bricks(setting, Vector2(74, 1), Vector2(8, 3), disp, 'grey'))
        self.bricks.append(bricks(setting, Vector2(82, 10), Vector2(18, 2), disp, 'grey'))
        self.bricks.append(bricks(setting, Vector2(90, 8), Vector2(3, 2), disp, 'grey'))
        self.bricks.append(bricks(setting, Vector2(96, 8), Vector2(4, 2), disp, 'grey'))
        self.bricks.append(bricks(setting, Vector2(96, 1), Vector2(4, 2), disp, 'grey'))
        self.bridge = boss_bridge(setting, Vector2(100, 8), 12, disp)
        self.lavas.append(liquid(setting,Vector2(100, 10), Vector2(12, 2), disp, False))
        self.bricks.append(bricks(setting, Vector2(112, 7), Vector2(3, 5), disp, 'grey'))
        self.bricks.append(bricks(setting, Vector2(113, 1), Vector2(2, 3), disp, 'grey'))
        self.bricks.append(bricks(setting, Vector2(115, 10), Vector2(13, 2), disp, 'grey'))

    def get_rect(self):
        x = list()
        for mybrick in self.bricks:
            x.append(mybrick.get_rect())
        for lava in self.lavas:
            x.append(lava.get_rect())

        return x

    def draw(self):
        self.disp.fill(Color('#000000'))
        for brick in self.bricks:
            brick.draw()
        for lava in self.lavas:
            lava.draw()
        self.bridge.draw()

    def move(self, delta):
        for brick in self.bricks:
            brick.move(delta)
        for lava in self.lavas:
            lava.move(delta)
        self.bridge.move(delta)