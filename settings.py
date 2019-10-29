import pygame
from pygame.math import Vector2

class Settings:
    """Manages game settings"""

    def __init__(self):
        """Initialize game settings"""

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

        # Map tiles
        self.map_tile = 16

        # sprite pages
        self.block_filename = "image/custom.png"
        self.block_filename_vector = Vector2(26, 24)

        self.brick = (4)
        self.brick_destroy = (32)
        self.brick_debris_L = (33)
        self.brick_debris_R = (34)

        self.question_block = (0, 1, 2)

        # pipes
        self.pipe_entr_top_h = (14, 15)
        self.pipe_tube_top_h = (40, 41)

        self.pipe_entr_bot_h = (118, 119)
        self.pipe_tube_bot_h = (40, 41)

        self.pipe_entr_left_v = (80, 105)
        self.pipe_tube_left_v = (81, 106)

        self.pipe_entr_right_v = (80, 105)
        self.pipe_tube_right_v = (81, 106)
        pass

    def get_frame_list(self, path, count=1):
        """Returns a list of image files."""
        return [pygame.transform.scale2x(pygame.image.load(path + '/{}.png'.format(i))) for i in range(0,count)]