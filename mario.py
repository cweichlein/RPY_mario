import pygame
from pygame.sprite import Sprite
import math


class Mario(Sprite):
    def __init__(self, settings, screen, stats, scoreboard):
        super(Mario, self).__init__(settings, screen, stats, scoreboard)  # initialize superclass object
        self.settings = settings  # save passed objects for local access
        self.screen = screen
        self.stats = stats
        self.scoreboard = scoreboard

        self.screen_rect = screen.get_rect()  # gets the passed screen object's rectangle
        # self.image = IMPLEMENT!
        self.rect = self.image.get_rect()  # gets the image's rectangle
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False
        self.die = False

    def update(self):
        if not self.die:
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.center += self.ai_settings.ship_speed_factor
            if self.moving_left and self.rect.left > 0:
                self.center -= self.ai_settings.ship_speed_factor
            self.rect.centerx = math.floor(self.center)

    # draws mario image at the current position of self.rect
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx