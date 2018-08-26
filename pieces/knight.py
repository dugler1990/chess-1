import pygame
from pieces import template


class Knight(template.Template):

    def __init__(self, location, color):
        template.Template.__init__(self, location, color)

        self.ID = 'N'
        self.image_a = pygame.image.load('pieces/img/White N.png')
        self.image_b = pygame.image.load('pieces/img/Black N.png')

    def _update(self):

        pass

