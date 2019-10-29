import pygame
from pygame.sprite import Sprite
import math

from timer import Timer


class Mario(Sprite):
    def __init__(self, settings, screen, blocks):
        super(Mario, self).__init__()  # initialize superclass object
        self.settings = settings  # save passed objects for local access
        self.screen = screen
        self.blocks = blocks

        self.screen_rect = screen.get_rect()  # gets the passed screen object's rectangle
        self.image = pygame.image.load('image/mario/mario/stand_right/0.png')
        self.rect = self.image.get_rect()  # gets the image's rectangle
        #self.mario_gravity = settings.mario_gravity
        self.horizSpeed = float(0)
        self.vertSpeed = float(0)
        self.die = False
        self.respawn = False
        self.jump_potential_energy_max = 30
        self.jump_potential_energy = 0

    def change_speed(self, h, v):
        self.horizSpeed += float(h)
        self.vertSpeed += float(v)

    def jump_set_potential_energy(self, landed):
        if landed:
            self.jump_potential_energy = self.jump_potential_energy_max

    def update(self):
        if not self.die:
            self.rect.x += self.horizSpeed
            collidable_list = pygame.sprite.spritecollide(self, self.blocks, False)
            for collided_object in collidable_list:
                if self.horizSpeed > 0:
                    self.rect.right = collided_object.rect.left
                elif self.horizSpeed < 0:
                    self.rect.left = collided_object.rect.right
            self.rect.y += self.vertSpeed
            landed = False
            collidable_list2 = pygame.sprite.spritecollide(self, self.blocks, False)
            for collided_object in collidable_list2:
                if self.vertSpeed > 0:
                    self.rect.bottom = collided_object.rect.top
                    landed = True
                elif self.vertSpeed < 0:
                    self.rect.top = collided_object.rect.bottom
            if landed:
                self.vertSpeed = 0
                # self.jump_potential_energy()
            else:
                self.vertSpeed = 1

    # draws mario image at the current position of self.rect
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        print(self.rect.centerx)
