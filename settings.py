from pygame.math import Vector2

class Settings:
    """Manages game settings"""

    def __init__(self):
        """Initialize game settings"""
        # Map tiles
        self.map_tile = 16

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
        pass