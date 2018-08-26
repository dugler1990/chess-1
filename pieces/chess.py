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
        self._image = pygame.image.load('pieces/img/board.png')

        self.highlightedSquares = pygame.image.load('pieces/img/clear.png')

    def findMoves(self, piece):

        list = []

        if piece.ID == 'P':
            #print('clicked pawn')
            W = 1
            B = -1

            if piece.color == WHITE:

                x = [piece.location[0], piece.location[1] - W]

                list.append(x)
                if not piece.hasMoved:
                    list.append([piece.location[0], piece.location[1] - W * 2])

                check_a = [piece.location[0] - 1, piece.location[1] - W]
                check_b = [piece.location[0] + 1, piece.location[1] - W]

                for otherPiece in self.chessSet.pieces:

                    if otherPiece.location == check_a and otherPiece.color == B:
                        list.append(check_a)
                    if otherPiece.location == check_b and otherPiece.color == B:
                        list.append(check_b)

            if piece.color == BLACK:

                x = [piece.location[0], piece.location[1] - B]

                list.append(x)
                if not piece.hasMoved:
                    list.append([piece.location[0], piece.location[1] - B * 2])

                check_a = [piece.location[0] - 1, piece.location[1] - B]
                check_b = [piece.location[0] + 1, piece.location[1] - B]

                for otherPiece in self.chessSet.pieces:

                    if otherPiece.location == check_a and otherPiece.color == W:
                        list.append(check_a)
                    if otherPiece.location == check_b and otherPiece.color == W:
                        list.append(check_b)

            return list


        elif piece.ID == 'K':
            #print('clicked king')
            pass
        elif piece.ID == 'N':
            #print('clicked knight')
            pass
        elif piece.ID == 'Q':
            #print('clicked queen')
            pass
        elif piece.ID == 'R':
            #print('clicked rook')
            pass
        elif piece.ID == 'B':
            #print('clicked bishop')
            pass


        return list

    def update(self):

        for event in pygame.event.get():
            # If the user clicks
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Check if any pieces are active
                l = []
                for p in self.chessSet.pieces:
                    if p.active: l.append(1)

                # If there are no active pieces
                if len(l) == 0:

                    # Go through all the pieces, and find the one the mouse is over
                    #

                    # Loop through all the pieces
                    for piece in self.chessSet.pieces:

                        # If the mouse is over the current piece, run it's click() function
                        if mouseOver([piece.location[0] * self.gridSize, piece.location[1] * self.gridSize, 64, 64]):

                            # Clear the list of spaces to highlight
                            self.moveSquares = []
                            # Run the piece's click() function
                            piece.click()


                    for piece in self.chessSet.pieces:
                        if piece.active:
                            self.moveSquares = self.findMoves(piece)




        for piece in self.chessSet.pieces:
            piece.update()


    def draw(self):

        # Re-draw the board
        self.image = self._image

        # Draw the pieces
        for piece in self.chessSet.pieces:
            loc = [piece.location[0] * self.gridSize, piece.location[1] * self.gridSize]
            pygame.Surface.blit(self.image, piece.image, loc)

        # Clear the highlightesSpaces image
        self.highlightedSquares = pygame.image.load('pieces/img/clear.png')

        # Find the spaces to highlight
        for piece in self.chessSet.pieces:
            if piece.active:
                self.moveSquares = self.findMoves(piece)

        # Draw red squares around all the highlighted spces
        for square in self.moveSquares:
            rect = [square[0] * self.gridSize,
                    square[1] * self.gridSize,
                    self.gridSize,
                    self.gridSize]
            pygame.draw.rect(self.highlightedSquares, (255, 0, 0), rect, 2)

        pygame.Surface.blit(self.image, self.highlightedSquares, [0, 0])
