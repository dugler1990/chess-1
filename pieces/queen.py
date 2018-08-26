import pygame
from pieces import template


class Queen(template.Template):

    def __init__(self, location, color):
        template.Template.__init__(self, location, color)

        self.ID = 'Q'
        self.image_a = pygame.image.load('pieces/img/White Q.png')
        self.image_b = pygame.image.load('pieces/img/Black Q.png')

    def _update(self):

        pass

