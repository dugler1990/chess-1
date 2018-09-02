import pygame

import colors
from pieces import template


class Queen(template.Template):

    def __init__(self, location, color):
        template.Template.__init__(self, location, color)

        self.ID = 'Q'
        self.image_a = pygame.image.load('pieces/img/White Q.png')
        self.image_b = pygame.image.load('pieces/img/Black Q.png')

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

        x = self.location[0]
        y = self.location[1]

        self.moveSquares.clear()

        _list = [
            [[0, 0], True],
            [[0, 0], True],
            [[0, 0], True],
            [[0, 0], True],
            [[0, 0], True],
            [[0, 0], True],
            [[0, 0], True],
            [[0, 0], True],
        ]

        for n in range(1, 8):

            list = [
                [[x - n, y - n], _list[0][1]],
                [[x, y - n], _list[1][1]],
                [[x + n, y - n], _list[2][1]],
                [[x - n, y], _list[3][1]],
                [[x + n, y], _list[4][1]],
                [[x - n, y + n], _list[5][1]],
                [[x, y + n], _list[6][1]],
                [[x + n, y + n], _list[7][1]],
            ]

            print(list)

            for r in range(len(list)):

                space = list[r]
                ADD = True

                for piece in piecesAll:

                    if piece.location == space[0] and not piece.captured:
                        _list[r][1] = False

                        if piece.color == self.color:
                            ADD = False

                if ADD and space[1]:
                    self.moveSquares.append(space[0])






