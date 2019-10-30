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
<<<<<<< Updated upstream
=======
        self.respawn = False
        self.jump_potential_energy_max = 30
        self.jump_potential_energy = 0

    def new_blocks(self, list_of_rect):



    def change_speed(self, h, v):
        self.horizSpeed += float(h)
        self.vertSpeed += float(v)
>>>>>>> Stashed changes

    def jump_set_potential_energy(self, landed):
        if landed:
            self.jump_potential_energy = self.jump_potential_energy_max

    def update(self, list_rect):
        if not self.die:
<<<<<<< Updated upstream
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.center += self.ai_settings.ship_speed_factor
            if self.moving_left and self.rect.left > 0:
                self.center -= self.ai_settings.ship_speed_factor
            self.rect.centerx = math.floor(self.center)
=======
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
>>>>>>> Stashed changes

    # draws mario image at the current position of self.rect
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx