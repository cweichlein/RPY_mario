from sprite_sheet import spriteSheet
from pygame.math import Vector2
from settings import Settings
from pygame.sprite import Sprite
from pygame import display
from pygame import *
from pygame.sprite import *

class mario:
    def __init__(self, pos: Vector2, disp: display):
        self.rect = Rect(pos.x, pos.y, 16, 16)
        self.pos = pos
        self.disp = disp
        self.velocity = Vector2(0, 0)
        self.max_speed = .5
        self.jump_speed = .4
        self.jump_accel = self.max_speed / 2
        self.run_accel = self.max_speed / 2
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        self.jump = False
        self.jumped = False
        self.movement = 0
        self.count = 0

    def draw(self):
        #self.disp.fill(Color('#f0f0f0'))
        draw.rect(self.disp, Color('#ff00f0'), self.rect)

    def move(self, delta, rect_list):
        # horizontal movement
        if self.move_right and not self.move_left:
            if self.velocity.x < self.max_speed:
                self.velocity.x += (self.run_accel * (delta / 1000))
                if self.rect.right < 270:
                    self.pos.x += min(self.velocity.x, self.max_speed)
        elif self.move_left and not self.move_right:
            if self.rect.left >= 0:
                if self.velocity.x > -self.max_speed:
                    self.velocity.x += -(self.run_accel * (delta / 1000))
                    if self.velocity.x < 0:
                        self.pos.x += max(self.velocity.x, -self.max_speed)
            else:
                self.velocity.x = 0
        # vertical movement
        if self.jump and not self.move_down and not self.jumped:
            self.velocity.y = -self.jump_accel
            self.jump = False
            self.jumped = True

        if True:
            if self.velocity.y <= self.max_speed:
                self.velocity.y += (self.run_accel * (delta / 1000))
            self.pos.y += min(self.velocity.y, self.max_speed)
        self.count += 1
        for rect in rect_list:
            for rect1 in rect:
                if self.check_collision(rect1):
                    clip_rect = self.rect.clip(rect1)
                    print('Clipped Rect: ', clip_rect.width, 'count: ', self.count)
                    self.rect.centerx
                    if clip_rect.width > clip_rect.height:
                        if self.velocity.y < 0:
                            self.pos.y = rect1.y + 17
                            self.velocity.y = 0
                        else:
                            self.pos.y = rect1.y - 17
                            self.velocity.y = 0
                            self.jumped = False
                    elif clip_rect.height > clip_rect.width:
                        if self.velocity.x < 0:
                            self.pos.x = rect1.x + 17
                            self.velocity.x = 0
                        else:
                            self.pos.x = rect1.x - 17
                            self.velocity.x = 0
                    else:  # hit perfect corner
                        if self.velocity.y > 0 and self.velocity.x > 0:
                            self.pos.x -= clip_rect.width
                            self.pos.y -= clip_rect.height
                            self.velocity.x = 0
                            self.velocity.y = 0
                        elif self.velocity.y > 0 and self.velocity.x < 0:
                            self.pos.x += clip_rect.width
                            self.pos.y -= clip_rect.height
                            self.velocity.x = 0
                            self.velocity.y = 0
                        elif self.velocity.y < 0 and self.velocity.x < 0:
                            self.pos.x -= clip_rect.width
                            self.pos.y += clip_rect.height
                            self.velocity.x = 0
                            self.velocity.y = 0
                        elif self.velocity.y < 0 and self.velocity.x < 0:
                            self.pos.x += clip_rect.width
                            self.pos.y += clip_rect.height
                            self.velocity.x = 0
                            self.velocity.y = 0
                        self.rect.x = self.pos.x
                        self.rect.y = self.pos.y


                    # if self.velocity.y < 0:
                    #     self.pos.y = rect1.y + 16
                    #     # self.velocity.y = 0
                    # elif self.velocity.y > 0:
                    #     self.pos.y = rect1.y - 16
                    #     # self.velocity.y = 0
                    #     self.jump = False
                    # if self.velocity.x > 0:
                    #     self.pos.x = rect1.x + 16
                    #     # self.velocity.x = 0
                    # elif self.velocity.x < 0:
                    #     self.pos.x = rect1.x - 16
                    #     # self.velocity.x = 0
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

        if self.velocity.x > self.max_speed:
            self.movement = self.max_speed
        else:
            self.movement = self.velocity.x

    def check_collision(self, rect: Rect):
        return rect.colliderect(self.rect)