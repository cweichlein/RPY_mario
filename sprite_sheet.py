import pygame
from pygame.math import Vector2

class spriteSheet:

    def __init__(self, filename, dim: Vector2):

        self.sheet = pygame.image.load(filename)
        self.row = dim.y
        self.col = dim.x
        self.cell_count = dim.y * dim.x
        self.rect = self.sheet.get_rect()

        w = self.cell_width = self.rect.width / dim.x
        h = self.cell_height = self.rect.height / dim.y
        hw, hh = self.cell_center = (w / 2, h / 2)

        self.cells = list([((index % dim.x) * w, (index // dim.x) * h, w, h) for index in range(self.cell_count)])

    def draw(self, surface, cell_index, pos: Vector2):
        surface.blit(self.sheet, (pos.x, pos.y), self.cells[cell_index])