from pygame.math import Vector2

class Settings:
    """Manages game settings"""

    def __init__(self):
        """Initialize game settings"""
        # Map tiles
        self.map_tile = 16

<<<<<<< Updated upstream
        # sprite pages
        self.block_filename = "image/custom.png"
        self.block_filename_vector = Vector2(28,24)

        self.brick = tuple(3)
        self.brick_destroy = tuple(32)
        self.brick_debris_L = tuple(33)
        self.brick_debris_R = tuple(34)

        self.question_block = tuple(0,1,2)

        # pipes
        self.pipe_entr_top_h = tuple(15,16)
        self.pipe_tube_top_h = tuple(40,41)

        self.pipe_entr_bot_h = tuple(15,16)
        self.pipe_tube_bot_h = tuple(40,41)

        self.pipe_entr_left_v = tuple(80,105)
        self.pipe_tube_left_v = tuple(81,106)

        self.pipe_entr_right_v = tuple(80,105)
        self.pipe_tube_right_v = tuple(81,106)
=======
        # scroll
        self.scroll_speed = -.25

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

        self.pipe_entr_right_v = (68, 94)
        self.pipe_tube_right_v = (65, 91)

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

        # coral
        self.coral_index = 316

        # lava
        self.lava_index = 237
        self.lava_surface_index = 211
>>>>>>> Stashed changes
        pass