import pygame
import time
from config import *
from board import Board
from solver import bfs

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

font = pygame.font.SysFont("arial", 40, bold=True)
win_font = pygame.font.SysFont("arial", 30, bold=True)
info_font = pygame.font.SysFont("arial", 28)

board = Board()
board.shuffle()
start_time = time.time()

# ======================
# AI Solver
# ======================
ai_path = []
ai_step = 0
ai_solving = False

AI_DELAY = 250  # milliseconds
last_ai_move = 0

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

            # ======================
            # Shuffle game
            # ======================
            if event.key == pygame.K_s:
                board.shuffle()
                start_time = time.time()

                ai_path = []
                ai_step = 0
                ai_solving = False

            # ======================
            # Solve by BFS
            # ======================
            elif event.key == pygame.K_b:
                ai_path = bfs(board.get_state())

                if ai_path and len(ai_path) > 1:
                    ai_step = 1
                    ai_solving = True
                    last_ai_move = pygame.time.get_ticks()

    # ======================
    # AI AUTO MOVE (nếu cần chạy)
    # ======================
    if ai_solving:
        now = pygame.time.get_ticks()

        if now - last_ai_move > AI_DELAY:
            if ai_step < len(ai_path):
                board.set_state(ai_path[ai_step])
                ai_step += 1
                last_ai_move = now
            else:
                ai_solving = False

    # ======================
    # DRAW
    # ======================
    screen.fill(BACKGROUND_COLOR)

    # Moves
    move_text = info_font.render(
        f"Moves: {board.moves}",
        True,
        (255, 255, 255)
    )
    screen.blit(move_text, (20, 20))

    # Time
    elapsed = int(time.time() - start_time)
    minutes = elapsed // 60
    seconds = elapsed % 60

    time_text = info_font.render(
        f"Time: {minutes:02d}:{seconds:02d}",
        True,
        (255, 255, 255)
    )
    screen.blit(time_text, (20, 55))

    # ======================
    # DRAW BOARD
    # ======================
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
                    center=(x + TILE_SIZE // 2, y + TILE_SIZE // 2)
                )

                screen.blit(text, text_rect)

    # ======================
    # WIN CHECK
    # ======================
    if board.is_solved():
        text = win_font.render(
            "YOU WIN!",
            True,
            (0, 255, 0)
        )

        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, 50))
        screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()