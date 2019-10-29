import pygame
import math

from animation import Animation
from enemy import Enemy
from settings import Settings
from timer import Timer

class Troopa(Enemy):
    def __init__(self, screen, settings, x, y, player, floor, block, goombas, koopas):
        super().__init__(screen, settings, x, y, player, floor, block, goombas, koopas)

        self.animate_set_character(character='green_koopa_troopa', settings=settings)

    def upside_down_death_animation(self):
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

    def update(self):
        self.koopa_physics()
        self.update_animation()
        self.blitme()

    def check_player_shell_collision(self):
        # Check player collision when in shell
        if self.rect.colliderect(self.player.rect):
            return True

    def koopa_physics(self):
        """USE MARIO CURRENT POSITION TO GET LEFT OF SCREEN"""
        self.check_boundary()

        if not self.check_floor() and self.start_movement:
            self.rect.y += (abs(self.enemy_direction) * self.enemy_gravity)
            self.rect.x = self.rect.x + (self.enemy_direction * (self.enemy_speed - 1))
        if self.check_floor() and self.start_movement:
            self.rect.x = self.rect.x + (self.enemy_direction * self.enemy_speed)

        # If collision
        if self.check_collisions():
            # Gets stomped on -> stop
            # Collides with player when in shell -> Movement
            if self.enemy_player_collide_flag and self.shell_mode:
                time = pygame.time.get_ticks()
                # Only put in shell if needed
                if self.death_animation_frame == 0:
                    self.animate(name_of_animation='in_shell')
                    tempx, tempy = self.rect.x, self.rect.y
                    self.rect = self.image.get_rect()
                    self.rect.x = tempx
                    self.rect.y = tempy
                    self.death_animation_frame += 1
                # Collide with player in shell mode causes movement
                if self.check_player_shell_collision():
                    self.shell_movement = True
                # Move shell depending on which side was hit
                if self.shell_movement:
                    if self.death_animation_frame == 1:
                        # Left side was hit
                        if self.rect.x >= self.player.rect.x:
                            self.enemy_direction = abs(self.enemy_direction)
                        # Right side hit
                        else:
                            self.enemy_direction = abs(self.enemy_direction) * -1
                        self.death_animation_frame += 1
                    if self.check_block_collision():
                        pass
                    self.rect.x += (self.enemy_direction * self.enemy_speed)
                # Not being hit by player again makes koopa pop out of shell
                if not self.check_player_shell_collision() and abs(self.last_frame - time) > 8000 and not\
                        self.shell_movement:
                    if self.counter == 0:
                        '''
                        self.animator = Animator(self.feet_images)
                        '''
                        self.feet_frame = pygame.time.get_ticks()
                        self.counter += 1
                    if abs(self.feet_frame - time) > 3000:
                        self.counter = 0
                        self.enemy_direction = abs(self.enemy_direction) * -1
                        self.animate(name_of_animation='walk_left')
                        self.enemy_player_collide_flag = False
                        self.shell_mode = False
            # Collision with map or block
            elif self.enemy_block_collide_flag:
                # Killed by player hitting block
                if self.block_enemy_kill:
                    self.dead = True
                    self.animate(name_of_animation='upside_down')
                # If colliding with map (i.e. Pipe) change direction
                else:
                    self.rect.x += (self.enemy_direction * self.enemy_speed)
                    self.enemy_block_collide_flag = False
            # If colliding with goomba change direction
            elif self.enemy_goomba_collide_flag:
                self.rect.x += (self.enemy_direction * self.enemy_speed)
                self.enemy_goomba_collide_flag = False
            elif self.enemy_koopa_collide_flag:
                # Colliding with koopa shell thats moving
                if self.shell_enemy_kill:
                    self.dead = True
                    self.animate(name_of_animation='upside_down')
                # Colliding with koopa enemy or shell
                else:
                    self.rect.x += (self.enemy_direction * self.enemy_speed)
                    self.enemy_koopa_collide_flag = False