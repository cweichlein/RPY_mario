import pygame
from pygame.sprite import Sprite
import math

from timer import Timer


class Mario(Sprite):
    def __init__(self, screen, settings):
        super(Mario, self).__init__()  # initialize superclass object
        self.settings = settings  # save passed objects for local access
        self.screen = screen


        self.base_frame = None
        self.walk_right_frames = None
        self.walk_left_frames = None
        self.image = None
        self.prepare_animation()

        self.screen_rect = screen.get_rect()  # gets the passed screen object's rectangle
        self.rect = self.image.get_rect()  # gets the image's rectangle
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.centery
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False
        self.die = False

        self.timer = Timer(frames=self.base_frame)

    def prepare_animation(self):
        self.base_frame = [pygame.image.load('image/mario/base/right.png')]
        self.walk_right_frames = [pygame.image.load('image/mario/walk_right/{}.png'.format(i)) for i in range(0,4)]
        self.walk_left_frames = [pygame.image.load('image/mario/walk_left/{}.png'.format(i)) for i in range(0,4)]
        self.image = self.base_frame[0]

    def walk_right(self):
        self.timer.frames = self.walk_right_frames

    def walk_left(self):
        self.timer.frames = self.walk_left_frames

    def update(self):
        if not self.die:
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.center += self.ai_settings.ship_speed_factor
            if self.moving_left and self.rect.left > 0:
                self.center -= self.ai_settings.ship_speed_factor
            self.rect.centerx = math.floor(self.center)

        self.walk_left()
        self.image = self.timer.image_rect()


    # draws mario image at the current position of self.rect
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx