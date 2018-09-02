import pygame

import colors
from pieces import template


class Knight(template.Template):

    def __init__(self, location, color):
        template.Template.__init__(self, location, color)

        self.ID = 'N'
        self.image_a = pygame.image.load('pieces/img/White N.png')
        self.image_b = pygame.image.load('pieces/img/Black N.png')

        if self.color == (255, 255, 255): self.image = self.image_a
        elif self.color == (0, 0, 0): self.image = self.image_b

    def findSpaces(self, piecesAll):

        self.active = True
        self.moveSquares.clear()

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

        x = self.location[0]
        y = self.location[1]

        list = [
            [x-1, y-2],
            [x+1, y-2],
            [x+2, y-1],
            [x-2, y-1],
            [x-2, y+1],
            [x+2, y+1],
            [x-1, y+2],
            [x+1, y+2],

        ]

        for space in list:

            ADD = True

            for piece in piecesAll:

                if piece.location == space and piece.color == self.color and not piece.captured:
                    ADD = False
                elif not (0 <= space[0] <= 7) or not (0 <= space[1] <= 7):
                    ADD = False

            if ADD:
                self.moveSquares.append(space)






