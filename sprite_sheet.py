import pygame
from pygame.math import Vector2

class spriteSheet:

    def __init__(self, filename, dim: Vector2):

        self.sheet = pygame.image.load(filename)
        self.row = int(dim.y)
        self.col = int(dim.x)
        self.cell_count = int(dim.y * dim.x)
        self.rect = self.sheet.get_rect()

        w = self.cell_width = int(self.rect.width / dim.x)
        h = self.cell_height = int(self.rect.height / dim.y)
        hw, hh = self.cell_center = (w / 2, h / 2)

        self.cells = list([((index % int(dim.x)) * w, (index // int(dim.x)) * h, w, h) for index in range(self.cell_count)])

    def draw(self, surface, cell_index: int, pos: Vector2):
        surface.blit(self.sheet, (int(pos.x), int(pos.y)), self.cells[cell_index])
