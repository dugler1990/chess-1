import pygame
import colors
from pieces import template


class Pawn(template.Template):

    def __init__(self, location, color):
        template.Template.__init__(self, location, color)

        self.ID = 'P'
        self.image_a = pygame.image.load('pieces/img/White P.png')
        self.image_b = pygame.image.load('pieces/img/Black P.png')

        if self.color == (255, 255, 255): self.image = self.image_a
        elif self.color == (0, 0, 0): self.image = self.image_b

    def findSpaces(self, piecesAll):

        self.active = True

        # Find all the possible spaces a pawn can move to given
        # any position, and any configuration of other pieces.

        # White is + because it is on the bottom,
        # and the y value has to decrease to go up.
        W = -1

        # Black is - because it is on the top,
        # and the y value has to increase to go down.
        B = 1

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

        # -------------------------
        # Search for spaces

        # Find the space in front of the piece
        ADD = True
        x = [self.location[0], self.location[1] - COLOR]

        # If any other pieces are already in that space
        for piece in piecesAll:
            if piece.location == x and not piece.captured:
                # Don't add the space
                ADD = False

        # Add the space if it is empty
        if ADD:
            self.moveSquares.append(x)

        # -------------------------
        # A pawn can go 2 spaces forward on it's first move
        if not self.hasMoved:
            ADD = True
            x = [self.location[0], self.location[1] - COLOR * 2]

            # If any other pieces are already in that space
            for piece in piecesAll:
                if piece.location == x:
                    # Don't add the space
                    ADD = False

            # Add the space if it is empty
            if ADD:
                self.moveSquares.append(x)

        # -------------------------
        # Get the coordinates for the front-left and front-right to
        # check for enemies to attack.
        check_a = [self.location[0] - 1, self.location[1] - COLOR]
        check_b = [self.location[0] + 1, self.location[1] - COLOR]

        for otherPiece in piecesAll:

            # If there is an enemy in either space
            if otherPiece.location == check_a and otherPiece.color != self.color:
                # Add it to the list
                self.moveSquares.append(check_a)
            if otherPiece.location == check_b and otherPiece.color != self.color:
                self.moveSquares.append(check_b)

        # -------------------------
        # Check if there is an enemy pawn to the left or right of the piece
        # If there is, the piece can move to the upper left/right corner

        frontLeft = [self.location[0] - 1, self.location[1] - COLOR]
        frontRight = [self.location[0] + 1, self.location[1] - COLOR]
        left = [self.location[0] - 1, self.location[1]]
        right = [self.location[0] + 1, self.location[1]]

        for piece in piecesAll:

            # If any of the other pieces are enemy pawns, and not captured
            if piece.color != self.color and piece.ID == 'P' and not piece.captured:

                # Add the space behind them to the list
                if piece.location == left: self.moveSquares.append(frontLeft)
                elif piece.location == right: self.moveSquares.append(frontRight)




