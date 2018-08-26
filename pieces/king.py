import pygame
from pieces import template


class King(template.Template):

    def __init__(self, location, color):
        template.Template.__init__(self, location, color)

        self.ID = 'K'
        self.image_a = pygame.image.load('pieces/img/White K.png')
        self.image_b = pygame.image.load('pieces/img/Black K.png')

    def _update(self):

        pass