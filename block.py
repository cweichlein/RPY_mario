from sprite_sheet import spriteSheet
from pygame.math import Vector2
from settings import Settings
from pygame import display
from pygame import *

class brick:
    def __init__(self, setting: Settings, pos: Vector2, disp: display):
        self.disp = disp
        self.brick = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile
        self.brick_index = setting.brick
        self.brick_break = setting.brick_destroy
        self.brick_debris_L = setting.brick_debris_L
        self.brick_debris_R = setting.brick_debris_R

    def draw(self):
        self.brick.draw(self.disp, self.brick_index, self.pos)
    pass
class bricks:
    def __init__(self, setting: Settings, origin: Vector2, count: int, disp: display, horz: bool):
        self.bricks = list()
        if horz:
            self.bricks = [brick(setting, Vector2(origin.x + x, origin.y), disp) for x in range(count)]
            print([Vector2(origin.x + x, origin.y)for x in range(count)])
        else:
            self.bricks = [brick(setting, Vector2(origin.x, origin.y + x), disp) for x in range(count)]

    def draw(self):
        for mybrick in self.bricks:
            mybrick.draw()
    pass

class question:
    def __init__(self, setting: Settings, pos: Vector2, disp: display):
        self.disp = disp
        self.question = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile
        self.question_block = setting.question_block
        self.index = 0
        self.anim_len = len(self.question_block)
        self.hit = False

    def draw(self):
        if self.hit:
            if self.index > self.anim_len:
                self.index += 1
            self.question.draw(self.disp, self.question_block[self.index], self.pos)
        else:
            self.question.draw(self.disp,self.question_block[0], self.pos)

class questions:
    pass

class pipe:
    def __init__(self, setting: Settings, pos: Vector2, dim: Vector2, disp: display, horz: bool, top: bool, left: bool):
        self.disp = disp
        self.setting = setting
        self.pipe = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile
        self.dim = dim
        self.rect = list()
        for x in range(1, int(dim.x + 1)):
            for y in range(1, int(dim.y + 1)):
                 self.rect.append(Rect(pos.x + self.pipe.cell_width * x, pos.y + self.pipe.cell_height * y, self.pipe.cell_width, self.pipe.cell_height))

        if horz:
            if top:
                self.pipe_entr = setting.pipe_entr_top_h
                self.pipe_tube = setting.pipe_tube_top_h
            else:
                self.pipe_entr = setting.pipe_entr_bot_h
                self.pipe_tube = setting.pipe_tube_bot_h
        else:
            if left:
                self.pipe_entr = setting.pipe_entr_left_v
                self.pipe_tube = setting.pipe_tube_left_v
            else:
                self.pipe_entr = setting.pipe_entr_right_v
                self.pipe_tube = setting.pipe_tube_right_v

        self.horz = horz
        self.top = top
        self.left = left

    def draw(self):
        for rect in self.rect:
            pass
            # draw.rect(self.disp, Color('#ffffff'), rect)
        if self.horz:
            if self.top:
                count = 0
                for entr in self.pipe_entr:
                    self.pipe.draw(self.disp, entr, Vector2(self.pos.x + self.setting.map_tile * count, self.pos.y))
                    count += 1
                for x in range(1, int(self.dim.y)):
                    count = 0
                    for tube in self.pipe_tube:
                        self.pipe.draw(self.disp, tube,Vector2(self.pos.x + self.setting.map_tile * count, self.pos.y + 16 * x))
                        count += 1
            else:
                for x in range(int(self.dim.y)):
                    count = 0
                    for tube in self.pipe_tube:
                        self.pipe.draw(self.disp, tube, Vector2(self.pos.x + self.setting.map_tile * count, self.pos.y + 16 * x))
                        count += 1
                count = 0
                for entr in self.pipe_entr:
                    self.pipe.draw(self.disp, entr, Vector2(self.pos.x + self.setting.map_tile * count, self.pos.y * self.dim.y))
                    count += 1
                pass
        else:
            if self.left:
                for x in range(1, int(self.dim.y)):
                    count = 0
                    for tube in self.pipe_tube:
                        self.pipe.draw(self.disp, tube,Vector2(self.pos.x + self.setting.map_tile * x, self.pos.y + self.setting.map_tile * count))
                        count += 1
                pass
            else:
                for x in range(1, int(self.dim.y)):
                    count = 0
                    for tube in self.pipe_tube:
                        self.pipe.draw(self.disp, tube,Vector2(self.pos.x + self.setting.map_tile * x, self.pos.y + self.setting.map_tile * count))
                        count += 1
                pass

class invincible_block:
    pass
class invincible_blocks:
    pass
class tree:
    pass
class bridge:
    pass
class coral:
    pass
class cloud:
    pass
class vine:
    pass
class coin:
    pass
class water:
    pass
class water_surface:
    pass
class mushroom_block:
    pass