from pieces import pawn
from pieces import king
from pieces import queen
from pieces import bishop
from pieces import rook
from pieces import knight
import colors

import pygame

def mouseOver(rect):
    m = pygame.mouse.get_pos()
    if rect[0] < m[0] < rect[0] + rect[2]:
        if rect[1] < m[1] < rect[1] + rect[3]:
            return True
    return False

class ChessSet:

    def __init__(self):

        self.colors = [colors.PLAYER_1, colors.PLAYER_2]

        self.pieces = [
            # PLAYER_1 pieces

            pawn.Pawn([0, 6], self.colors[1]),
            pawn.Pawn([1, 6], self.colors[1]),
            pawn.Pawn([2, 6], self.colors[1]),
            pawn.Pawn([3, 6], self.colors[1]),
            pawn.Pawn([4, 6], self.colors[1]),
            pawn.Pawn([5, 6], self.colors[1]),
            pawn.Pawn([6, 6], self.colors[1]),
            pawn.Pawn([7, 6], self.colors[1]),

            rook.Rook([0, 7], self.colors[1]),
            rook.Rook([7, 7], self.colors[1]),

            knight.Knight([1, 7], self.colors[1]),
            knight.Knight([6, 7], self.colors[1]),

            bishop.Bishop([2, 7], self.colors[1]),
            bishop.Bishop([5, 7], self.colors[1]),

            queen.Queen([3, 7], self.colors[1]),
            king.King([4, 7], self.colors[1]),

            # PLAYER_2 pieces

            pawn.Pawn([0, 1], self.colors[0]),
            pawn.Pawn([1, 1], self.colors[0]),
            pawn.Pawn([2, 1], self.colors[0]),
            pawn.Pawn([3, 1], self.colors[0]),
            pawn.Pawn([4, 1], self.colors[0]),
            pawn.Pawn([5, 1], self.colors[0]),
            pawn.Pawn([6, 1], self.colors[0]),
            pawn.Pawn([7, 1], self.colors[0]),

            rook.Rook([0, 0], self.colors[0]),
            rook.Rook([7, 0], self.colors[0]),

            knight.Knight([1, 0], self.colors[0]),
            knight.Knight([6, 0], self.colors[0]),

            bishop.Bishop([2, 0], self.colors[0]),
            bishop.Bishop([5, 0], self.colors[0]),

            queen.Queen([3, 0], self.colors[0]),
            king.King([4, 0], self.colors[0]),
        ]

class Board:

    class Space:

        def __init__(self, color):
            self.color = color
            self.contents = None

    def __init__(self, gridSize):

        self.gridSize = gridSize
        self.chessSet = ChessSet()
        self.image = pygame.image.load('pieces/img/board.png')
        self.SELECT_FLAG = False

    def getMouse(self):

        m = pygame.mouse.get_pos()

        x = int(m[0] / self.gridSize)
        y = int(m[1] / self.gridSize)

        return [x, y]

    def update(self):

        for event in pygame.event.get():

            # Exit when exit button is pushed
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # If the user clicks
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                # If there is already a piece selected
                if self.SELECT_FLAG:

                    # Find the active piece
                    for piece in self.chessSet.pieces:
                        if piece.active:

                            # If the mouse is over the active piece
                            if piece.location == self.getMouse():

                                # Deselect the piece
                                self.SELECT_FLAG = False
                                piece.active = False

                            else:

                                # Else if the mouse is over any of the piece's selected squares
                                for space in piece.moveSquares:
                                    if space == self.getMouse():

                                        # Move the piece to the space
                                        piece.move(space, self.chessSet.pieces)
                                        self.SELECT_FLAG = False

                                        # Keep the space on the board
                                        if piece.location[0] < 0: piece.location[0] = 0
                                        if piece.location[1] < 0: piece.location[1] = 0
                                        if piece.location[0] > 7: piece.location[0] = 7
                                        if piece.location[1] > 7: piece.location[1] = 7

                                        # If there is an enemy in the new space
                                        # DELETE IT!
                                        for otherPiece in self.chessSet.pieces:
                                            if space == otherPiece.location:
                                                if otherPiece.color != piece.color:
                                                    otherPiece.captured = True

                # If there is no piece selected yet
                elif not self.SELECT_FLAG:

                    # Go through all the pieces
                    for piece in self.chessSet.pieces:

                        # If the mouse is over an active piece
                        if piece.location == self.getMouse() and not piece.captured:

                            # Select and move the piece
                            self.SELECT_FLAG = True
                            piece.findSpaces(self.chessSet.pieces)

    def draw(self):

        #squareWidth = 4
        squareWidth = 0

        # Reset the board image
        self.image = pygame.image.load('pieces/img/board.png')
        # -------------------------
        # Draw red squares around all the spaces onto the board image
        for piece in self.chessSet.pieces:
            if piece.active:

                for square in piece.moveSquares:
                    # Create a rectangle from the coordinates
                    rect = [square[0] * self.gridSize,
                            square[1] * self.gridSize,
                            self.gridSize,
                            self.gridSize]

                    # Draw the square
                    pygame.draw.rect(self.image, (128, 0, 0), rect, squareWidth)
        # -------------------------
        # Draw a blue square around the selected piece
        # Create a rectangle from the coordinates
        for piece in self.chessSet.pieces:
            if piece.active:
                rect = [piece.location[0] * self.gridSize,
                        piece.location[1] * self.gridSize,
                        self.gridSize,
                        self.gridSize]

                # Draw the square
                pygame.draw.rect(self.image, (0, 128, 0), rect, squareWidth)

        # -------------------------
        # Draw the pieces
        for piece in self.chessSet.pieces:

            # If the piece hasn't been captured
            if not piece.captured:
                # Find it's location and draw it's image
                loc = [piece.location[0] * self.gridSize, piece.location[1] * self.gridSize]
                pygame.Surface.blit(self.image, piece.image, loc)
