from pieces import pawn
from pieces import king
from pieces import queen
from pieces import bishop
from pieces import rook
from pieces import knight

import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def mouseOver(rect):
    m = pygame.mouse.get_pos()
    if rect[0] < m[0] < rect[0] + rect[2]:
        if rect[1] < m[1] < rect[1] + rect[3]:
            return True
    return False

class ChessSet:

    def __init__(self):

        self.colors = [BLACK, WHITE]

        self.pieces = [

            # Black pieces

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

            # White pieces

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

        ]

class Board:

    class Space:

        def __init__(self, color):
            self.color = color
            self.contents = None

    def __init__(self, gridSize):

        self.gridSize = gridSize
        self.chessSet = ChessSet()
        self.moveSquares = []
        self.image = pygame.image.load('pieces/img/board.png')

    def findMoves(self, piece):

        list = []

        if piece.ID == 'P':

            # Find all the possible spaces a pawn can move to given
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
            if piece.color == WHITE: COLOR = W
            if piece.color == BLACK: COLOR = B

            x = [piece.location[0], piece.location[1] - COLOR]

            list.append(x)

            # A pawn can go 2 spaces forward on it's first move
            if not piece.hasMoved:
                list.append([piece.location[0], piece.location[1] - COLOR * 2])

            # Get the coordinates for the front-left and front-right to
            # check for enemies to attack.
            check_a = [piece.location[0] - 1, piece.location[1] - COLOR]
            check_b = [piece.location[0] + 1, piece.location[1] - COLOR]

            for otherPiece in self.chessSet.pieces:

                if otherPiece.location == check_a and otherPiece.color == W:
                    list.append(check_a)
                if otherPiece.location == check_b and otherPiece.color == W:
                    list.append(check_b)

        elif piece.ID == 'K':   # King
            #print('clicked king')
            pass
        elif piece.ID == 'N':   # Knight
            #print('clicked knight')
             pass
        elif piece.ID == 'Q':   # Queen
            #print('clicked queen')
            pass
        elif piece.ID == 'R':   # Rook
            #print('clicked rook')
            pass
        elif piece.ID == 'B':   # Bishop
            #print('clicked bishop')
            pass

        return list

    def update(self):

        for event in pygame.event.get():

            # If the user clicks
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Selecting and de-selecting a piece
                # ---------------

                # Look for any active pieces
                l = []
                for p in self.chessSet.pieces:
                    if p.active: l.append(p)

                # If there are no active pieces
                if len(l) == 0:

                    # Go through all the pieces, and find the one the mouse is over
                    #

                    # Loop through all the pieces
                    for piece in self.chessSet.pieces:

                        # If the mouse is over the current piece
                        if mouseOver([piece.location[0] * self.gridSize, piece.location[1] * self.gridSize, 64, 64]):

                            # Clear the list of spaces to highlight
                            self.moveSquares = []
                            # Run the piece's click() function to activate it
                            piece.click()

                    # Find the active piece, and find it's possible moves
                    for piece in self.chessSet.pieces:
                        if piece.active:
                            self.moveSquares = self.findMoves(piece)

                    # Find the spaces to highlight
                    for piece in self.chessSet.pieces:
                        if piece.active:
                            self.moveSquares = self.findMoves(piece)

                # If there is an active piece
                else:

                    piece = l[0]

                    # If the mouse is over the currently active piece
                    if mouseOver([piece.location[0] * self.gridSize, piece.location[1] * self.gridSize, self.gridSize, self.gridSize]):

                        # Run it's click() function to de-activate it
                        piece.click()

                        # Clear the moveSquares list
                        self.moveSquares.clear()

                    else:

                        # Check all the selected squares
                        for space in self.moveSquares:
                            loc_x = space[0] * self.gridSize
                            loc_y = space[1] * self.gridSize
                            width = self.gridSize
                            height = self.gridSize

                            # If the mouse is over a selected square
                            if mouseOver([loc_x, loc_y, width, height]):
                                piece.move([space[0], space[1]])
                                piece.click()
                                self.moveSquares.clear()





        # Update all the pieces
        for piece in self.chessSet.pieces:
            piece.update()

    def draw(self):

        # Reset the board image
        self.image = pygame.image.load('pieces/img/board.png')

        # Draw the pieces
        for piece in self.chessSet.pieces:
            loc = [piece.location[0] * self.gridSize, piece.location[1] * self.gridSize]
            pygame.Surface.blit(self.image, piece.image, loc)

        # If there are spaces to highlight
        if len(self.moveSquares):

            # Draw red squares around all the spaces onto the board image
            for square in self.moveSquares:

                # Create a rectangle from the coordinates
                rect = [square[0] * self.gridSize,
                        square[1] * self.gridSize,
                        self.gridSize,
                        self.gridSize]

                # Draw the square
                pygame.draw.rect(self.image, (255, 0, 0), rect, 3)

