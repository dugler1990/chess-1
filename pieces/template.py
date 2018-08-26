import pygame

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

class Template:

    def __init__(self, location, color):
        self.ID = ''
        self.image = pygame.Surface((0, 0))
        self.color = color
        self.location = location
        self.hasMoved = False
        self.active = False

    def _update(self): pass  # Leave empty for custom update

    def update(self):

        if self.color == (255, 255, 255): self.image = self.image_a
        elif self.color == (0, 0, 0): self.image = self.image_b
        self._update()

    def click(self):

        self.active = True

    def move(self, spaces, gridSize, highlightedSquares):

        pass