import pygame
from config import *
from board import Board

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

font = pygame.font.SysFont("arial", 40, bold=True)
win_font = pygame.font.SysFont("arial", 30, bold=True)

board = Board()
board.shuffle()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            mx, my = pygame.mouse.get_pos()

            col = (mx - BOARD_X) // (TILE_SIZE + TILE_GAP)
            row = (my - BOARD_Y) // (TILE_SIZE + TILE_GAP)

            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
                index = row * BOARD_SIZE + col
                board.move(index)

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_s:
                board.shuffle()

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
                text_rect = text.get_rect(
                    center=(x + TILE_SIZE // 2,
                            y + TILE_SIZE // 2)
                )
                screen.blit(text, text_rect)

    # Kiểm tra chiến thắng
    if board.is_solved():
        text = win_font.render("YOU WIN!", True, (0, 255, 0))
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, 50))
        screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()