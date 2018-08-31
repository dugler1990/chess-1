import pygame
from pieces import template
import colors


class Bishop(template.Template):

    def __init__(self, location, color):
        template.Template.__init__(self, location, color)

        self.ID = 'B'
        self.image_a = pygame.image.load('pieces/img/White B.png')
        self.image_b = pygame.image.load('pieces/img/Black B.png')

        if self.color == (255, 255, 255): self.image = self.image_a
        elif self.color == (0, 0, 0): self.image = self.image_b


    def findSpaces(self, piecesAll):

        self.active = True

        # Find all the possible spaces a king can move to given
        # any position, and any configuration of other pieces.

        # White is + because it is on the bottom,
        # and the y value has to decrease to go up.
        W = 1

        # Black is - because it is on the top,
        # and the y value has to increase to go down.
        B = -1

        # Color is set to the appropriate B/W value
        # from above according to it's color.
        #
        # Multiply it [B/W] with the number of
        # spaces forward the piece moves.
        COLOR = 0

        # Color is set to the piece's color
        if self.color == colors.PLAYER_1:
            COLOR = W
        elif self.color == colors.PLAYER_2:
            COLOR = B






