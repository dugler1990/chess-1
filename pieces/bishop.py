import pygame
from pieces import template


class Bishop(template.Template):

    def __init__(self, location, color):
        template.Template.__init__(self, location, color)

        self.ID = 'B'
        self.image_a = pygame.image.load('pieces/img/White B.png')
        self.image_b = pygame.image.load('pieces/img/Black B.png')

    def _update(self):

        pass

