import pygame
import colors

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
        self.captured = False
        self.moveSquares = []

    def findSpaces(self, piecesAll): pass


    def move(self, location, piecesAll):

        self.hasMoved = True

        self.moveSquares.clear()
        self.location = location

        if self.location[0] < 0: self.location[0] = 0
        elif self.location[0] > 7: self.location[0] = 7
        if self.location[1] < 0: self.location[1] = 0
        elif self.location[1] > 7: self.location[1] = 7

        self.active = False
