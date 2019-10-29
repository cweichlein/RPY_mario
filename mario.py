import pygame
from pygame.sprite import Sprite
import math

from animation import Animation
from timer import Timer

class Mario(Sprite, Animation):
    def __init__(self, screen, settings):
        super(Mario, self).__init__()  # initialize superclass object
        self.settings = settings  # save passed objects for local access
        self.screen = screen

        self.animate_set_character(character='mario', settings=settings)

        self.screen_rect = screen.get_rect()  # gets the passed screen object's rectangle
        self.rect = self.image.get_rect()  # gets the image's rectangle
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.centery
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False
        self.die = False

    def update(self):
        self.animate(name_of_animation='jump_right')
        self.update_animation()
        self.blitme()
    # draws mario image at the current position of self.rect
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx