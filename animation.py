import pygame
from timer import Timer

class Animation:
    """Handles character animations."""

    def __init__(self):
        self.dict_of_frames = None
        self.image = None
        self.timer = None

    def no_frames_error(self, name):
        raise KeyError('No ' + name + ' animation in that character\'s animations.')

    def animate_set_character(self, character, settings):
        """Sets the character to use for animations."""
        if character in settings.character_frames:
            self.dict_of_frames = settings.character_frames[character]
            self.image = self.dict_of_frames['base'][0]
            self.timer = Timer(self.dict_of_frames['base'])

    def animate(self, name_of_animation):
        if name_of_animation in self.dict_of_frames:
            self.timer.frames = self.dict_of_frames[name_of_animation]
        
        else:
            self.no_frames_error(name_of_animation)

    def update_animation(self):
        """Updates the character's image."""
        self.image = self.timer.image_rect()