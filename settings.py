from pygame.math import Vector2
import pygame

class Settings:
    """Manages game settings"""

    def __init__(self):
        """Initialize game settings"""
        # Map tiles
        self.map_tile = 16

        # scroll
        self.scroll_speed = -.25

        self.character_frames = {
            'mario': {
                'base': self.get_frame_list(path='image/mario/mario/stand_right', count=1),
                'stand_right': self.get_frame_list(path='image/mario/mario/stand_right', count=1),
                'stand_left': self.get_frame_list(path='image/mario/mario/stand_left', count=1),
                'walk_right': self.get_frame_list(path='image/mario/mario/walk_right', count=3),
                'walk_left': self.get_frame_list(path='image/mario/mario/walk_left', count=3),
                'jump_right': self.get_frame_list(path='image/mario/mario/jump_right', count=1),
                'jump_left': self.get_frame_list(path='image/mario/mario/jump_left', count=1)
            },
            'super_mario': {
                'base': self.get_frame_list(path='image/mario/super_mario/stand_right', count=1),
                'stand_right': self.get_frame_list(path='image/mario/super_mario/stand_right', count=1),
                'stand_left': self.get_frame_list(path='image/mario/super_mario/stand_left', count=1),
                'walk_right': self.get_frame_list(path='image/mario/super_mario/walk_right', count=3),
                'walk_left': self.get_frame_list(path='image/mario/super_mario/walk_left', count=3),
                'jump_right': self.get_frame_list(path='image/mario/super_mario/jump_right', count=1),
                'jump_left': self.get_frame_list(path='image/mario/super_mario/jump_left', count=1),
                'crouch_left': self.get_frame_list(path='image/mario/super_mario/crouch_left', count=1),
                'crouch_right': self.get_frame_list(path='image/mario/super_mario/crouch_right', count=1)
            },
            'fire_mario': {
                'base': self.get_frame_list(path='image/mario/fire_mario/stand_right', count=1),
                'stand_right': self.get_frame_list(path='image/mario/fire_mario/stand_right', count=1),
                'stand_left': self.get_frame_list(path='image/mario/fire_mario/stand_left', count=1),
                'walk_right': self.get_frame_list(path='image/mario/fire_mario/walk_right', count=3),
                'walk_left': self.get_frame_list(path='image/mario/fire_mario/walk_left', count=3),
                'jump_right': self.get_frame_list(path='image/mario/fire_mario/jump_right', count=1),
                'jump_left': self.get_frame_list(path='image/mario/fire_mario/jump_left', count=1),
                'crouch_left': self.get_frame_list(path='image/mario/fire_mario/crouch_left', count=1),
                'crouch_right': self.get_frame_list(path='image/mario/fire_mario/crouch_right', count=1)
            },
            'invin_mario': {
                'base': self.get_frame_list(path='image/mario/invin_mario/stand_right', count=4),
                'stand_right': self.get_frame_list(path='image/mario/invin_mario/stand_right', count=4),
                'stand_left': self.get_frame_list(path='image/mario/invin_mario/stand_left', count=4),
                'walk_right': self.get_frame_list(path='image/mario/invin_mario/walk_right', count=4),
                'walk_left': self.get_frame_list(path='image/mario/invin_mario/walk_left', count=4),
                'jump_right': self.get_frame_list(path='image/mario/invin_mario/jump_right', count=4),
                'jump_left': self.get_frame_list(path='image/mario/invin_mario/jump_left', count=4),
                'crouch_left': self.get_frame_list(path='image/mario/invin_mario/crouch_left', count=4),
                'crouch_right': self.get_frame_list(path='image/mario/invin_mario/crouch_right', count=4)
            },
            'goomba': {
                'base': self.get_frame_list(path='image/enemies/goomba/base', count=1),
                'walk': self.get_frame_list(path='image/enemies/goomba/walk', count=2),
                'upside_down': self.get_frame_list(path='image/enemies/goomba/upside_down', count=1),
                'crushed': self.get_frame_list(path='image/enemies/goomba/crushed', count=1)
            },
            'blue_goomba': {
                'base': self.get_frame_list(path='image/enemies/goomba/blue_goomba/base', count=1),
                'walk': self.get_frame_list(path='image/enemies/goomba/blue_goomba/walk', count=2),
                'upside_down': self.get_frame_list(path='image/enemies/goomba/blue_goomba/upside_down', count=1),
                'crushed': self.get_frame_list(path='image/enemies/goomba/blue_goomba/crushed', count=1)
            },
            'gray_goomba': {
                'base': self.get_frame_list(path='image/enemies/goomba/gray_goomba/base', count=1),
                'walk': self.get_frame_list(path='image/enemies/goomba/gray_goomba/walk', count=2),
                'upside_down': self.get_frame_list(path='image/enemies/goomba/gray_goomba/upside_down', count=1),
                'crushed': self.get_frame_list(path='image/enemies/goomba/gray_goomba/crushed', count=1)
            },
            'green_koopa_troopa': {
                'base': self.get_frame_list(path='image/enemies/koopa_troopa/green/base', count=1),
                'walk_right': self.get_frame_list(path='image/enemies/koopa_troopa/green/walk_right', count=2),
                'walk_left': self.get_frame_list(path='image/enemies/koopa_troopa/green/walk_left', count=2),
                'upside_down': self.get_frame_list(path='image/enemies/koopa_troopa/green/upside_down', count=1),
                'in_shell': self.get_frame_list(path='image/enemies/koopa_troopa/green/in_shell', count=1),
            },
            'red_koopa_troopa': {
                'base': self.get_frame_list(path='image/enemies/koopa_troopa/red/base', count=1),
                'walk_right': self.get_frame_list(path='image/enemies/koopa_troopa/red/walk_right', count=2),
                'walk_left': self.get_frame_list(path='image/enemies/koopa_troopa/red/walk_left', count=2),
                'upside_down': self.get_frame_list(path='image/enemies/koopa_troopa/red/upside_down', count=1),
                'in_shell': self.get_frame_list(path='image/enemies/koopa_troopa/red/in_shell', count=1),

            }
        }

        # Enemy Settings
        self.enemy_direction = -1
        self.enemy_gravity = 4
        self.enemy_speed = 2

        # sprite pages
        self.block_filename = "image/custom.png"
        self.block_filename_vector = Vector2(26, 24)

        self.brick_gold = (4)
        self.brick_destroy_gold = (32)
        self.brick_debris_L_gold = (33)
        self.brick_debris_R_gold = (34)

        self.brick_blue = (338)
        self.brick_destroy_blue = (32)
        self.brick_debris_L_blue = (33)
        self.brick_debris_R_blue = (34)

        self.brick_grey = (234)
        self.brick_destroy_grey = (32)
        self.brick_debris_L_grey = (33)
        self.brick_debris_R_grey = (34)

        self.question_block = (0, 1, 2)

        # pipes
        self.pipe_entr_top_h = (14, 15)
        self.pipe_tube_top_h = (40, 41)

        self.pipe_entr_bot_h = (118, 119)
        self.pipe_tube_bot_h = (40, 41)

        self.pipe_entr_left_v = (64, 90)
        self.pipe_tube_left_v = (65, 91)
        self.pipe_link_left_v = (66, 92)

        self.pipe_entr_right_v = (68, 94)
        self.pipe_tube_right_v = (65, 91)
        self.pipe_link_right_v = (67, 93)

        # self.pipe_dark_green =
        # self.pipe_lite_green =
        # self.pipe_dark_brown =
        # self.pipe_lite_silvr =

        # invincible block
        self.invincible_block_index = 53

        # floor block
        self.floor_block_index = 52

        # bridge
        self.bridge_block_index = (107, 108, 109)
        self.bridge_fence_index = (81, 82, 83)

        self.boss_bridge_block_index = 238
        self.boss_bridge_chain_index = 212

        # mushroom
        self.mushroom_top_green_index = (84, 85, 86)
        self.mushroom_top_orange_index = (110, 111, 112)
        self.mushroom_mid_index = 137
        self.mushroom_bot_index = 163

        # cliff
        self.cliff_top_index = (78, 79, 80)
        self.cliff_mid_index = (104, 105, 106)
        self.cliff_bot_index = (130, 131, 132)

        # water
        self.water_index = 315
        self.water_surface_index = 317

        # lava
        self.lava_index = 237
        self.lava_surface_index = 211

        # coral
        self.coral_index = 316

        # cloud
        self.cloud_index = 420

        # vine
        self.vine_green_index = 419, 445
        self.vine_blue_index = 418, 444

        # coin
        self.coin_reg_index = 26, 27, 28
        self.coin_cav_index = 286, 287, 288
        self.coin_wat_index = 390, 391, 392


        # castle
        self.castle_index = 521, 522, 523, 524, 547, 548, 549
        self.castle_flag_index = 489

        # metel platform
        self.Ibeam_index = 290, 291, 292

        # pully ropes
        self.rope_index = 263, 264, 265, 289
        # axe
        self.axe_index = 213, 214, 215

        # flag
        self.flag_index = 495
        self.flag_poll_index = 470, 496
        self.flag_height = 8

        # bush
        self.bush_index = (10, 11, 12)

        # tree
        self.small_tree_index = (32, 58)
        self.large_tree_index = (7, 33, 59)

        # hedge
        self.small_hedge_index = 34
        self.large_hedge_index = (9, 35)

        # fence
        self.fence_index = (54, 55, 56)

        # cannon
        self.cannon_index = 138, 164, 190

        #spring
        self.up_spring_index = 113, 139
        self.reg_spring_index = 114, 140
        self.down_spring_index = 141



    def get_frame_list(self, path, count=1):
        """Returns a list of image files."""
        return [pygame.transform.scale2x(pygame.image.load(path + '/{}.png'.format(i))) for i in range(0, count)]
    pass