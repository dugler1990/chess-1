import pygame
from pieces import template


class Rook(template.Template):

    def __init__(self, location, color):
        template.Template.__init__(self, location, color)

        self.ID = 'R'
        self.image_a = pygame.image.load('pieces/img/White R.png')
        self.image_b = pygame.image.load('pieces/img/Black R.png')

    def _update(self):

        pass

