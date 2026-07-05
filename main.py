import pygame
from config import *
from board import Board

pygame.init()

board = Board()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

font = pygame.font.SysFont("arial", 40, bold=True)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):

            index = row * BOARD_SIZE + col
            value = board.get_value(index)

            x = BOARD_X + col * (TILE_SIZE + TILE_GAP)
            y = BOARD_Y + row * (TILE_SIZE + TILE_GAP)

            pygame.draw.rect(
                screen,
                TILE_COLOR,
                (x, y, TILE_SIZE, TILE_SIZE)
            )

            pygame.draw.rect(
                screen,
                LINE_COLOR,
                (x, y, TILE_SIZE, TILE_SIZE),
                2
            )

            if value != 0:
                text = font.render(str(value), True, TEXT_COLOR)
                text_rect = text.get_rect(center=(x + TILE_SIZE // 2, y + TILE_SIZE // 2))
                screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()