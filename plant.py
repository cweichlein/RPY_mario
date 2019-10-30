import pygame
import math

from animation import Animation
from enemy import Enemy
from settings import Settings
from timer import Timer

class Plant(Enemy, Animation):
    def __init__(self, screen, settings, x, y, player, floor, block, goombas, koopas):
        super().__init__(screen, settings, x, y, player, floor, block, goombas, koopas)

        self.animate_set_character(character='plant', settings=settings)

    def pop_up_animation(self):
        time = pygame.time.get_ticks()
        # Animate and keep on screen
        self.rect.y -= (abs(self.enemy_direction) * self.enemy_speed)
        self.animate(name_of_animation='pop_up')
        # Disappear after after 1 second
        if abs(self.last_frame - time) > 1000:
            self.kill()


    def death_animation(self):
        time = pygame.time.get_ticks()
        # Animate getting hit (Go up for two seconds)
        if self.death_animation_frame == 0:
            self.rect.y += (abs(self.enemy_direction) * self.enemy_speed)
        else:
            self.rect.y += (abs(self.enemy_direction) * self.enemy_speed * -1)
        # After two seconds fall down while upside down
        if self.death_animation_frame == 0 and abs(self.last_frame - time) > 2000:
            self.animate(name_of_animation='upside_down')
            self.death_animation_frame += 1
        """MIGHT BE REDUNDANT WITH CHECK BOUNDARY"""
        # Kill off after 10 seconds (Enough to be off screen)
        if abs(self.last_frame - time) > 10000:
            self.player.score += 100
            self.kill()

    def update(self):
        if not self.dead:
            self.plant_physics()
        else:
            if self.player_enemy_kill is True:
                self.animate(name_of_animation='death')
        self.update_animation()
        self.blitme()

    def goomba_physics(self):
        if self.check_collisions():
            # Collides with player
            if self.enemy_player_collide_flag:
                # Enemy dead
                if self.player_enemy_kill:
                    self.dead = True
                    self.last_frame = pygame.time.get_ticks()
                    self.animate(name_of_animation='death')
                else:
                    self.enemy_player_collide_flag = False