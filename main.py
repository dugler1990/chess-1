import pygame
from pieces import chess

display = pygame.display.set_mode((1000, 800))

def main():

    gridSize = 64

    board = chess.Board(gridSize)

    board.draw()
    pygame.Surface.blit(display, board.image, (0, 0))
    pygame.display.update()

    while True:

        board.update()

        pygame.Surface.fill(display, (0, 0, 0))

        board.draw()

        pygame.draw.rect(display, (128, 128, 128), [209, 109, 582, 582], 0)
        pygame.Surface.blit(display, board.image, (244, 144))

        pygame.display.update()

main()