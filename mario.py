import pygame
from pygame.sprite import Sprite


class Mario(Sprite):
    def __init__(self, settings, screen, stats, scoreboard):
        super(Mario, self).__init__(settings, screen, stats, scoreboard)  # initialize superclass object
        self.settings = settings  # save passed objects for local access
        self.screen = screen
        self.stats = stats
        self.scoreboard = scoreboard
