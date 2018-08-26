import pygame
from pieces import template


class Pawn(template.Template):

    def __init__(self, location, color):
        template.Template.__init__(self, location, color)

        self.ID = 'P'
        self.image_a = pygame.image.load('pieces/img/White P.png')
        self.image_b = pygame.image.load('pieces/img/Black P.png')

    def _update(self):

        pass
