from pygame.math import Vector2

class Settings:
    """Manages game settings"""

    def __init__(self):
        """Initialize game settings"""
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