from sprite_sheet import spriteSheet
from pygame.math import Vector2
from settings import Settings
from pygame import display
from pygame import *

class brick:
<<<<<<< Updated upstream
    def __init__(self, setting: Settings, pos: Vector2, disp: display):
        self.disp = disp
        self.brick = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile
        self.brick_index = setting.brick
        self.brick_break = setting.brick_destroy
        self.brick_debris_L = setting.brick_debris_L
        self.brick_debris_R = setting.brick_debris_R

    def draw(self):
        self.brick.draw(self.disp,self.brick,self.pos)
    pass
class bricks:
    def __init__(self, setting: Settings,origin: Vector2, count: int, disp: display, horz: bool):
        self.bricks = list()
        if horz:
            self.bricks = [brick(setting,Vector2(origin.x + x, origin.y), disp) for x in range(count)]
        else:
            self.bricks = [brick(setting, Vector2(origin.x, origin.y + x), disp) for x in range(count)]

    def draw(self):
        for brick in self.bricks:
            brick.draw()
    pass
=======
    def __init__(self, setting: Settings, pos: Vector2, disp: display, brick_type: str):
        self.disp = disp
        self.setting = setting
        self.brick = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile

        if brick_type == 'gold':
            self.brick_index = setting.brick_gold
            self.brick_break = setting.brick_destroy_gold
            self.brick_debris_L = setting.brick_debris_L_gold
            self.brick_debris_R = setting.brick_debris_R_gold
            pass
        elif brick_type == 'blue':
            self.brick_index = setting.brick_blue
            self.brick_break = setting.brick_destroy_blue
            self.brick_debris_L = setting.brick_debris_L_blue
            self.brick_debris_R = setting.brick_debris_R_blue
            pass
        elif brick_type == 'grey':
            self.brick_index = setting.brick_grey
            self.brick_break = setting.brick_destroy_grey
            self.brick_debris_L = setting.brick_debris_L_grey
            self.brick_debris_R = setting.brick_debris_R_grey
            pass

    def draw(self):
        self.brick.draw(self.disp, self.brick_index, self.pos)

    def move(self):
        self.pos.x += self.setting.scroll_speed
    pass
class bricks:
    def __init__(self, setting: Settings, pos: Vector2, dim: Vector2, disp: display, brick_type: str):
        self.bricks = list()
        self.dim = dim
        if brick_type == 'gold':
            for x in range(int(self.dim.x)):
                for y in range(int(self.dim.y)):
                    self.bricks.append(brick(setting, Vector2(pos.x + x, pos.y + y), disp, 'gold'))

        elif brick_type == 'blue':
            for x in range(int(self.dim.x)):
                for y in range(int(self.dim.y)):
                    self.bricks.append(brick(setting, Vector2(pos.x + x, pos.y + y), disp, 'blue'))

        elif brick_type == 'grey':
            for x in range(int(self.dim.x)):
                for y in range(int(self.dim.y)):
                    self.bricks.append(brick(setting, Vector2(pos.x + x, pos.y + y), disp, 'grey'))

    def draw(self):
        for mybrick in self.bricks:
            mybrick.draw()

    def move(self):
        for mybrick in self.bricks:
            mybrick.move()
>>>>>>> Stashed changes

class question:
    def __init__(self, setting: Settings, pos: Vector2, disp: display):
        self.disp = disp
<<<<<<< Updated upstream
        self.question = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos
=======
        self.setting = setting
        self.question = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile
>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
class questions:
    pass
class pipe:

    def __init__(self, setting: Settings, pos: Vector2, dim: Vector2, disp: display, horz: bool, top: bool, left: bool):
        self.disp = disp
        self.pipe = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos
        self.dim = dim
        self.rect = [Rect(pos.x + self.pipe.cell_width * x, pos.y + self.pipe.cell_height * x,self.pipe.cell_width,self.pipe.cell_height)for x in range(dim.x * dim.y)]

=======
    def move(self):
        self.pos.x += self.setting.scroll_speed

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
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
        pygame.draw.rect(self.disp, Color('#ffffff'), self.rect)
=======
        for rect in self.rect:
            pass
            # draw.rect(self.disp, Color('#ffffff'), rect)
>>>>>>> Stashed changes
        if self.horz:
            if self.top:
                count = 0
                for entr in self.pipe_entr:
<<<<<<< Updated upstream
                    self.pipe.draw(self.disp, entr, Vector2(self.pos.x + 16 * count, self.pos.y))
                    count += 1
                for x in self.dim.y:
                    count = 0
                    for tube in self.pipe_tube:
                        self.pipe.draw(self.disp, tube,Vector2(self.pos.x + 16 * count, self.pos.y + 16 * x))
                        count =+ 1


class horz_pipe:
    pass
class invincible_block:
    pass
class invincible_blocks:
    pass
class tree:
    pass
class bridge:
    pass
=======
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
                for x in range(1, int(self.dim.x)):
                    count = 0
                    for tube in self.pipe_tube:
                        self.pipe.draw(self.disp, tube, Vector2(self.pos.x + self.setting.map_tile * x, self.pos.y + self.setting.map_tile * count))
                        count += 1
                count = 0
                for entr in self.pipe_entr:
                    self.pipe.draw(self.disp, entr, Vector2(self.pos.x, self.pos.y + self.setting.map_tile * count))
                    count += 1
            else:
                for x in range(int(self.dim.x - 1)):
                    count = 0
                    for tube in self.pipe_tube:
                        self.pipe.draw(self.disp, tube,Vector2(self.pos.x + self.setting.map_tile * x, self.pos.y + self.setting.map_tile * count))
                        count += 1
                count = 0
                for entr in self.pipe_entr:
                    self.pipe.draw(self.disp, entr, Vector2(self.pos.x + self.setting.map_tile * (self.dim.x - 1), self.pos.y + self.setting.map_tile * count))
                    count += 1
                pass

    def move(self):
        self.pos.x += self.setting.scroll_speed

class invincible_block:
    def __init__(self, setting: Settings, pos: Vector2, disp: display):
        self.disp = disp
        self.setting = setting
        self.brick = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile
        self.invincible_block_index = setting.invincible_block_index

    def draw(self):
        self.brick.draw(self.disp, self.invincible_block_index, self.pos)

    def move(self):
        self.pos.x += self.setting.scroll_speed
    pass

class invincible_blocks:
    def __init__(self, setting: Settings, pos: Vector2, count: int, disp: display, horz: bool):
        self.bricks = list()
        if horz:
            self.bricks = [invincible_block(setting, Vector2(pos.x + x, pos.y), disp) for x in range(count)]
        else:
            self.bricks = [invincible_block(setting, Vector2(pos.x, pos.y + x), disp) for x in range(count)]

    def draw(self):
        for mybrick in self.bricks:
            mybrick.draw()

    def move(self):
        for mybrick in self.bricks:
            mybrick.move()

class floor_block:
    def __init__(self, setting: Settings, pos: Vector2, disp: display):
        self.disp = disp
        self.setting = setting
        self.brick = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile
        self.floor_block_index = setting.floor_block_index

    def draw(self):
        self.brick.draw(self.disp, self.floor_block_index, self.pos)

    def move(self):
         self.pos.x += self.setting.scroll_speed

class floor_blocks:
    def __init__(self, setting: Settings, pos: Vector2, count: int, disp: display, horz: bool):
        self.bricks = list()
        if horz:
            self.bricks = [floor_block(setting, Vector2(pos.x + x, pos.y), disp) for x in range(count)]
        else:
            self.bricks = [floor_block(setting, Vector2(pos.x, pos.y + x), disp) for x in range(count)]

    def draw(self):
        for mybrick in self.bricks:
            mybrick.draw()

    def move(self):
        for mybrick in self.bricks:
            mybrick.move()
    pass

class tree:
    pass
class bridge:
    def __init__(self, setting: Settings, pos: Vector2, length: int, disp: display):
        self.disp = disp
        self.setting = setting
        self.brick = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile
        self.bridge_block_index = setting.bridge_block_index
        self.bridge_fence_index = setting.bridge_fence_index
        self.length = length

    def draw(self):
        self.brick.draw(self.disp, self.bridge_fence_index[0], Vector2(self.pos.x, self.pos.y - self.setting.map_tile))
        self.brick.draw(self.disp,self.bridge_block_index[0], self.pos)
        for x in range(1, self.length):
            self.brick.draw(self.disp, self.bridge_fence_index[1], Vector2(self.pos.x + self.setting.map_tile * x, self.pos.y - self.setting.map_tile))
            self.brick.draw(self.disp, self.bridge_block_index[1], Vector2(self.pos.x + self.setting.map_tile * x, self.pos.y))
        self.brick.draw(self.disp, self.bridge_fence_index[-1], Vector2(self.pos.x + self.setting.map_tile * self.length, self.pos.y - self.setting.map_tile))
        self.brick.draw(self.disp, self.bridge_block_index[-1], Vector2(self.pos.x + self.setting.map_tile * self.length, self.pos.y))

    def move(self):
         self.pos.x += self.setting.scroll_speed
    pass

class boss_bridge:
    def __init__(self, setting: Settings, pos: Vector2, length: int, disp: display):
        self.disp = disp
        self.setting = setting
        self.brick = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile
        self.boss_bridge_block_index = setting.boss_bridge_block_index
        self.boss_bridge_chain_index = setting.boss_bridge_chain_index
        self.length = length
        self.draw_chain = True

    def draw(self):
        if self.draw_chain:
            self.brick.draw(self.disp, self.boss_bridge_chain_index, Vector2(self.pos.x + self.setting.map_tile * (self.length - 1), self.pos.y - self.setting.map_tile))
        for x in range(self.length):
            self.brick.draw(self.disp, self.boss_bridge_block_index, Vector2(self.pos.x + self.setting.map_tile * x, self.pos.y))

    def move(self):
        self.pos.x += self.setting.scroll_speed



>>>>>>> Stashed changes
class coral:
    pass
class cloud:
    pass
class vine:
    pass
class coin:
    pass
<<<<<<< Updated upstream
class water:
    pass
class water_surface:
    pass
class mushroom_block:
=======
class liquid:
    def __init__(self, setting: Settings, pos: Vector2, dim: Vector2, disp: display, water: bool):
        self.disp = disp
        self.setting = setting
        self.brick = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile
        self.dim = dim

        if water:
            self.liquid_index = setting.water_index
            self.liquid_surface_index = setting.water_surface_index
        else:
            self.liquid_index = setting.lava_index
            self.liquid_surface_index = setting.lava_surface_index

    def draw(self):
        for x in range(int(self.dim.x)):
            self.brick.draw(self.disp, self.liquid_surface_index, Vector2(self.pos.x + self.setting.map_tile * x, self.pos.y))
            for y in range(1, int(self.dim.y)):
                self.brick.draw(self.disp, self.liquid_index, Vector2(self.pos.x + self.setting.map_tile * x, self.pos.y + self.setting.map_tile * y))

    def move(self):
        self.pos.x += self.setting.scroll_speed

class mushroom_block:
    def __init__(self, setting: Settings, pos: Vector2, dim: Vector2, disp: display, green: bool):
        self.disp = disp
        self.setting = setting
        self.brick = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile
        self.dim = dim

        if green:
            self.mushroom_top_index = setting.mushroom_top_green_index
        else:
            self.mushroom_top_index = setting.mushroom_top_orange_index
        self.mushroom_mid_index = setting.mushroom_mid_index
        self.mushroom_bot_index = setting.mushroom_bot_index

    def draw(self):
        self.brick.draw(self.disp, self.mushroom_top_index[0], Vector2(self.pos.x, self.pos.y))
        for x in range(1, int(self.dim.x - 1)):
            self.brick.draw(self.disp, self.mushroom_top_index[1], Vector2(self.pos.x + self.setting.map_tile * x, self.pos.y))
        self.brick.draw(self.disp, self.mushroom_top_index[-1], Vector2(self.pos.x + self.setting.map_tile * (self.dim.x - 1), self.pos.y))

        self.brick.draw(self.disp, self.mushroom_mid_index, Vector2(self.pos.x + self.setting.map_tile * (self.dim.x // 2), self.pos.y + self.setting.map_tile * 1))

        for y in range(2, int(self.dim.y)):
            self.brick.draw(self.disp, self.mushroom_bot_index,
                            Vector2(self.pos.x + self.setting.map_tile * (self.dim.x // 2),
                                    self.pos.y + self.setting.map_tile * y))

    def move(self):
        self.pos.x += self.setting.scroll_speed

        pass
class cliff:
    def __init__(self, setting: Settings, pos: Vector2, dim: Vector2, disp: display):
        self.disp = disp
        self.setting = setting
        self.brick = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile
        self.cliff_top_index = setting.cliff_top_index
        self.cliff_mid_index = setting.cliff_mid_index
        self.cliff_bot_index = setting.cliff_bot_index
        self.dim = dim

    def draw(self):
        self.brick.draw(self.disp, self.cliff_top_index[0], Vector2(self.pos.x, self.pos.y))
        for x in range(1, int(self.dim.x)):
            self.brick.draw(self.disp, self.cliff_top_index[1], Vector2(self.pos.x + self.setting.map_tile * x, self.pos.y))
        self.brick.draw(self.disp, self.cliff_top_index[-1], Vector2(self.pos.x + self.setting.map_tile * self.dim.x, self.pos.y))

        self.brick.draw(self.disp, self.cliff_mid_index[0], Vector2(self.pos.x, self.pos.y + self.setting.map_tile * 1))
        for x in range(1, int(self.dim.x)):
            self.brick.draw(self.disp, self.cliff_mid_index[1],Vector2(self.pos.x + self.setting.map_tile * x, self.pos.y + self.setting.map_tile * 1))
        self.brick.draw(self.disp, self.cliff_mid_index[-1], Vector2(self.pos.x + self.setting.map_tile * self.dim.x, self.pos.y + self.setting.map_tile * 1))

        for y in range(2, int(self.dim.y)):
            self.brick.draw(self.disp, self.cliff_bot_index[0], Vector2(self.pos.x, self.pos.y + self.setting.map_tile * y))
            for x in range(1, int(self.dim.x)):
                self.brick.draw(self.disp, self.cliff_bot_index[1],
                                Vector2(self.pos.x + self.setting.map_tile * x, self.pos.y + self.setting.map_tile * y))
            self.brick.draw(self.disp, self.cliff_bot_index[-1],
                            Vector2(self.pos.x + self.setting.map_tile * self.dim.x, self.pos.y + self.setting.map_tile * y))

    def move(self):
         self.pos.x += self.setting.scroll_speed


class hill:
>>>>>>> Stashed changes
    pass