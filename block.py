"""
Classes:
    brick,
    bricks,
    pipe,
    invincible_block,
    floor_blocks,
    question,
    bridge,
    cliff,
    mushroom_block,
    liquid,
    boss_bridge,
    plant,
    flag,
    vine,
    coin
"""

from sprite_sheet import spriteSheet
from pygame.math import Vector2
from settings import Settings
from pygame.sprite import Sprite
from pygame import display
from pygame import *
from pygame.sprite import *

class brick(Sprite):
    def __init__(self, setting: Settings, pos: Vector2, disp: display, brick_type: str):
        super(brick, self).__init__()
        self.disp = disp
        self.setting = setting
        self.brick = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile
        self.rect = Rect(pos.x, pos.y, setting.map_tile, setting.map_tile)
        self.image = pygame.image.load('image/invisable.png')
        self.sp_rect = self.image.get_rect()

        # self.rect.colliderect()

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
        elif brick_type == 'coral':
            self.brick_index = setting.coral_index
        elif brick_type == 'cloud':
            self.brick_index = setting.cloud_index
            pass

    def get_rect(self):
        return self.rect

    def draw(self):
        self.brick.draw(self.disp, self.brick_index, self.pos)

    def move(self, delta):
        self.pos.x += self.setting.scroll_speed * delta
        self.rect.x = self.pos.x
    pass

class bricks:
    def __init__(self, setting: Settings, pos: Vector2, dim: Vector2, disp: display, brick_type: str):
        self.bricks = list()
        self.dim = dim

        for x in range(int(self.dim.x)):
            for y in range(int(self.dim.y)):
                self.bricks.append(brick(setting, Vector2(pos.x + x, pos.y + y), disp, brick_type))

    def draw(self):
        for mybrick in self.bricks:
            mybrick.draw()

    def move(self, delta):
        for mybrick in self.bricks:
            mybrick.move(delta)

    def get_rect(self):
        x = list()
        for y in self.bricks:
            x.append(y.get_rect())
        return x

class question:
    def __init__(self, setting: Settings, pos: Vector2, disp: display):
        self.disp = disp
        self.setting = setting
        self.question = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile
        self.question_block = setting.question_block
        self.index = 0
        self.anim_len = len(self.question_block)
        self.hit = False
        self.rect = Rect(pos.x, pos.y, setting.map_tile, setting.map_tile)

    def draw(self):
        if self.hit:
            if self.index > self.anim_len:
                self.index += 1
            self.question.draw(self.disp, self.question_block[self.index], self.pos)
        else:
            self.question.draw(self.disp,self.question_block[0], self.pos)

    def move(self, delta):
        self.pos.x += self.setting.scroll_speed * delta

    def get_rect(self):
        return self.rect

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
                self.pipe_link = setting.pipe_link_left_v
            else:
                self.pipe_entr = setting.pipe_entr_right_v
                self.pipe_tube = setting.pipe_tube_right_v
                self.pipe_link = setting.pipe_link_right_v

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
                for x in range(1, int(self.dim.x - 2)):
                    count = 0
                    for tube in self.pipe_tube:
                        self.pipe.draw(self.disp, tube, Vector2(self.pos.x + self.setting.map_tile * x, self.pos.y + self.setting.map_tile * count))
                        count += 1
                count = 0
                for entr in self.pipe_entr:
                    self.pipe.draw(self.disp, entr, Vector2(self.pos.x, self.pos.y + self.setting.map_tile * count))
                    count += 1
                count = 0
                for link in self.pipe_link:
                    self.pipe.draw(self.disp, link, Vector2(self.pos.x + self.setting.map_tile * (self.dim.x - 2), self.pos.y + self.setting.map_tile * count))
                    count += 1
            else:
                for x in range(1, int(self.dim.x - 2)):
                    count = 0
                    for tube in self.pipe_tube:
                        self.pipe.draw(self.disp, tube, Vector2(self.pos.x + self.setting.map_tile * x, self.pos.y + self.setting.map_tile * count))
                        count += 1
                count = 0
                for entr in self.pipe_entr:
                    self.pipe.draw(self.disp, entr, Vector2(self.pos.x + self.setting.map_tile * (self.dim.x - 2), self.pos.y + self.setting.map_tile * count))
                    count += 1
                count = 0
                for link in self.pipe_link:
                    self.pipe.draw(self.disp, link, Vector2(self.pos.x, self.pos.y + self.setting.map_tile * count))
                    count += 1

    def move(self, delta):
        self.pos.x += self.setting.scroll_speed * delta

    def get_rect(self):
        return self.rect

class invincible_block:
    def __init__(self, setting: Settings, pos: Vector2, disp: display):
        self.disp = disp
        self.setting = setting
        self.brick = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile
        self.invincible_block_index = setting.invincible_block_index
        self.rect = Rect(pos.x, pos.y, setting.map_tile, setting.map_tile)

    def draw(self):
        self.brick.draw(self.disp, self.invincible_block_index, self.pos)

    def move(self, delta):
        self.pos.x += self.setting.scroll_speed * delta

    def get_rect(self):
        return self.rect

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

    def move(self, delta):
        for mybrick in self.bricks:
            mybrick.move()

    def get_rect(self):
        x = list()
        for y in self.bricks:
            x.append(y.get_rect())
        return x

class floor_block:
    def __init__(self, setting: Settings, pos: Vector2, disp: display):
        self.disp = disp
        self.setting = setting
        self.brick = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile
        self.floor_block_index = setting.floor_block_index
        self.rect = Rect(pos.x, pos.y, setting.map_tile, setting.map_tile)

    def draw(self):
        self.brick.draw(self.disp, self.floor_block_index, self.pos)

    def move(self, delta):
         self.pos.x += self.setting.scroll_speed * delta

    def get_rect(self):
        return self.rect


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

    def move(self, delta):
        for mybrick in self.bricks:
            mybrick.move(delta)

    def get_rect(self):
        x = list()
        for y in self.bricks:
            x.append(y.get_rect())
        return x


class bridge:
    def __init__(self, setting: Settings, pos: Vector2, length: int, disp: display):
        self.disp = disp
        self.setting = setting
        self.brick = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile
        self.bridge_block_index = setting.bridge_block_index
        self.bridge_fence_index = setting.bridge_fence_index
        self.length = length
        self.rect = [Rect(pos.x + setting.map_tile * x, pos.y, setting.map_tile, setting.map_tile) for x in range(self.length)]

    def draw(self):
        self.brick.draw(self.disp, self.bridge_fence_index[0], Vector2(self.pos.x, self.pos.y - self.setting.map_tile))
        self.brick.draw(self.disp, self.bridge_block_index[0], self.pos)
        for x in range(1, self.length):
            self.brick.draw(self.disp, self.bridge_fence_index[1], Vector2(self.pos.x + self.setting.map_tile * x, self.pos.y - self.setting.map_tile))
            self.brick.draw(self.disp, self.bridge_block_index[1], Vector2(self.pos.x + self.setting.map_tile * x, self.pos.y))
        self.brick.draw(self.disp, self.bridge_fence_index[-1], Vector2(self.pos.x + self.setting.map_tile * self.length, self.pos.y - self.setting.map_tile))
        self.brick.draw(self.disp, self.bridge_block_index[-1], Vector2(self.pos.x + self.setting.map_tile * self.length, self.pos.y))

    def move(self, delta):
         self.pos.x += self.setting.scroll_speed * delta

    def get_rect(self):
        return self.rect

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
        self.rect = [Rect(pos.x + setting.map_tile * x, pos.y, setting.map_tile, setting.map_tile) for x in range(self.length)]

    def draw(self):
        if self.draw_chain:
            self.brick.draw(self.disp, self.boss_bridge_chain_index, Vector2(self.pos.x + self.setting.map_tile * (self.length - 1), self.pos.y - self.setting.map_tile))
        for x in range(self.length):
            self.brick.draw(self.disp, self.boss_bridge_block_index, Vector2(self.pos.x + self.setting.map_tile * x, self.pos.y))

    def move(self, delta):
        self.pos.x += self.setting.scroll_speed * delta

    def get_rect(self):
        return self.rect

class vine:
    def __init__(self, setting: Settings, pos: Vector2, dim: Vector2, disp: display, vine_type: str, hang: bool):
        self.disp = disp
        self.setting = setting
        self.brick = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile
        self.rect = Rect(pos.x, pos.y, setting.map_tile, setting.map_tile)
        self.dim = dim
        self.hang = hang
        self.rect = [Rect(pos.x + setting.map_tile * x, pos.y + setting.map_tile * y, setting.map_tile, setting.map_tile) for x in
                     range(int(dim.x)) for y in range(int(dim.y))]

        if vine_type == 'blue':
            self.vine_index = setting.vine_blue_index
        elif vine_type == 'green':
            self.vine_index = setting.vine_green_index

    def draw(self):
        if self.hang:
            for x in range(int(self.dim.x)):
                for y in range(int(self.dim.y)):
                    self.brick.draw(self.disp, self.vine_index[-1], Vector2(self.pos.x + self.setting.map_tile * x, self.pos.y + self.setting.map_tile * y))
        else:
            for x in range(int(self.dim.x)):
                self.brick.draw(self.disp, self.vine_index[0],
                                Vector2(self.pos.x + self.setting.map_tile * x, self.pos.y))
                for y in range(1, int(self.dim.y)):
                    self.brick.draw(self.disp, self.vine_index[-1], Vector2(self.pos.x + self.setting.map_tile * x, self.pos.y + self.setting.map_tile * y))

    def move(self, delta):
        self.pos.x += self.setting.scroll_speed * delta

    def get_rect(self):
        return self.rect

class coin:
    def __init__(self, setting: Settings, pos: Vector2, disp: display, coin_type: str):
        self.disp = disp
        self.setting = setting
        self.brick = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile
        self.rect = Rect(pos.x, pos.y, setting.map_tile, setting.map_tile)

        if coin_type == 'reg':
            self.coin_index = setting.coin_reg_index
        elif coin_type == 'wat':
            self.coin_index = setting.coin_wat_index
        elif coin_type == 'cav':
            self.coin_index = setting.coin_cav_index

        self.coin_state = 0
        self.coin_size = len(self.coin_index)

    def draw(self):
        self.brick.draw(self.disp, self.coin_index[self.coin_state], self.pos)
        self.coin_state += 1
        if self.coin_state < self.coin_size:
            self.coin_state = 0

    def move(self, delta):
        self.pos.x += self.setting.scroll_speed * delta

    def get_rect(self):
        return self.rect

class liquid:
    def __init__(self, setting: Settings, pos: Vector2, dim: Vector2, disp: display, water: bool):
        self.disp = disp
        self.setting = setting
        self.brick = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile
        self.dim = dim
        self.rect = [Rect(pos.x + setting.map_tile * x, pos.y + setting.map_tile * y, setting.map_tile, setting.map_tile) for x in
                     range(int(dim.x)) for y in range(int(dim.y))]

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

    def move(self, delta):
        self.pos.x += self.setting.scroll_speed * delta

    def get_rect(self):
        return self.rect

class mushroom_block:
    def __init__(self, setting: Settings, pos: Vector2, dim: Vector2, disp: display, green: bool):
        self.disp = disp
        self.setting = setting
        self.brick = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile
        self.dim = dim
        self.rect = self.rect = [Rect(pos.x + setting.map_tile * x, pos.y, setting.map_tile, setting.map_tile) for x in range(int(dim.x))]

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

    def move(self, delta):
        self.pos.x += self.setting.scroll_speed * delta

    def get_rect(self):
        return self.rect

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
        self.rect = self.rect = [Rect(pos.x + setting.map_tile * x, pos.y, setting.map_tile, setting.map_tile) for x in
                                 range(int(dim.x))]

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

    def move(self, delta):
         self.pos.x += self.setting.scroll_speed * delta

    def get_rect(self):
        return self.rect

class hill:
    def __init__(self, setting: Settings, pos: Vector2, disp: display, brick_type: str):
        self.disp = disp
        self.setting = setting
        self.brick = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile
        self.rect = Rect(pos.x, pos.y, setting.map_tile, setting.map_tile)
    pass

class castle:
    def __init__(self, setting: Settings, pos: Vector2, disp: display, brick_type: str):
        self.disp = disp
        self.setting = setting
        self.brick = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile
    pass
class flag:
    def __init__(self, setting: Settings, pos: Vector2, disp: display):
        self.disp = disp
        self.setting = setting
        self.brick = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile

        self.flag_index = setting.flag_index
        self.flag_poll_index = setting.flag_poll_index
        self.flag_height = setting.flag_height
        self.flag_time = self.flag_height / 5
        self.flag_lower = 0
        self.rect = [Rect(pos.x, pos.y + setting.map_tile * x, setting.map_tile, setting.map_tile) for x in
                     range(self.flag_height)]

    def draw(self):
        self.brick.draw(self.disp, self.flag_poll_index[0], Vector2(self.pos.x, self.pos.y))
        for y in range(1, self.flag_height):
            self.brick.draw(self.disp, self.flag_poll_index[-1], Vector2(self.pos.x, self.pos.y + self.setting.map_tile * y))

        self.brick.draw(self.disp, self.flag_index, Vector2(self.pos.x - self.setting.map_tile + 6, self.pos.y + self.setting.map_tile * self.flag_lower))

    def move(self, delta):
        self.pos.x += self.setting.scroll_speed * delta
        if self.flag_lower < self.flag_height - 1:
            self.flag_lower += self.flag_time * delta * .001

    def get_rect(self):
        return self.rect

class plant:
    def __init__(self, setting: Settings, pos: Vector2, disp: display, plant_type: str):
        self.disp = disp
        self.setting = setting
        self.brick = spriteSheet(setting.block_filename, setting.block_filename_vector)
        self.pos = pos * setting.map_tile
        self.plant_type = plant_type

        if plant_type == 'smll_tree':
            self.plant_index = setting.small_tree_index
        elif plant_type == 'tall_tree':
            self.plant_index = setting.large_tree_index
        elif plant_type == 'smll_hedge':
            self.plant_index = setting.small_hedge_index
        elif plant_type == 'tall_hedge':
            self.plant_index = setting.large_hedge_index
        elif plant_type == 'bush':
            self.plant_index = setting.bush_index

        if plant_type == 'smll_hedge':
            self.plant_size = 1
        else:
            self.plant_size = len(self.plant_index)
        # self.plant_state = 0

    def draw(self):
        if self.plant_type == 'smll_tree':
            for x in range(self.plant_size):
                self.brick.draw(self.disp, self.plant_index[x], Vector2(self.pos.x, self.pos.y + self.setting.map_tile * x))
        elif self.plant_type == 'tall_tree':
            for x in range(self.plant_size):
                self.brick.draw(self.disp, self.plant_index[x], Vector2(self.pos.x, self.pos.y + self.setting.map_tile * x))
        elif self.plant_type == 'smll_hedge':
                self.brick.draw(self.disp, self.plant_index, Vector2(self.pos.x, self.pos.y))
        elif self.plant_type == 'tall_hedge':
            for x in range(self.plant_size):
                self.brick.draw(self.disp, self.plant_index[x], Vector2(self.pos.x, self.pos.y + self.setting.map_tile * x))
        elif self.plant_type == 'bush':
            for x in range(self.plant_size):
                self.brick.draw(self.disp, self.plant_index[x], Vector2(self.pos.x + self.setting.map_tile * x, self.pos.y))

    def move(self, delta):
        self.pos.x += self.setting.scroll_speed * delta