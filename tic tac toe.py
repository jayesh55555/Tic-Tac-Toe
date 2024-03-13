import pygame
import sys

pygame.init()

# Screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600  # Making the window rectangular
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tic Tac Toe')

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (13, 161, 146)
TEXT_COLOR = (255, 255, 255)  # Changing text color to white for better visibility
X_COLOR = (66, 66, 66)
O_COLOR = (242, 235, 211)

# Fonts
FONT = pygame.font.Font(None, 40)

# Game variables
CELL_SIZE = SCREEN_WIDTH // 3  # Ensuring cells are square and fit the screen width
GAME_OVER = False
PLAYER = "X"
BOARD = [["" for _ in range(3)] for _ in range(3)]

def draw_board():
    SCREEN.fill(BG_COLOR)
    for x in range(1, 3):
        pygame.draw.line(SCREEN, LINE_COLOR, (x * CELL_SIZE, 0), (x * CELL_SIZE, SCREEN_HEIGHT - 200), 10)
    for y in range(1, 3):
        pygame.draw.line(SCREEN, LINE_COLOR, (0, y * CELL_SIZE), (SCREEN_WIDTH, y * CELL_SIZE), 10)

def draw_marks():
    for row in range(3):
        for col in range(3):
            center = (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2)
            if BOARD[row][col] == "X":
                pygame.draw.line(SCREEN, X_COLOR, (center[0] - 40, center[1] - 40), (center[0] + 40, center[1] + 40), 15)
                pygame.draw.line(SCREEN, X_COLOR, (center[0] + 40, center[1] - 40), (center[0] - 40, center[1] + 40), 15)
            elif BOARD[row][col] == "O":
                pygame.draw.circle(SCREEN, O_COLOR, center, 40, 15)

def check_game_over():
    global GAME_OVER
    # Check rows, columns, and diagonals
    for row in range(3):
        if BOARD[row][0] == BOARD[row][1] == BOARD[row][2] != "":
            GAME_OVER = True
            return BOARD[row][0]
    for col in range(3):
        if BOARD[0][col] == BOARD[1][col] == BOARD[2][col] != "":
            GAME_OVER = True
            return BOARD[0][col]
    if BOARD[0][0] == BOARD[1][1] == BOARD[2][2] != "" or BOARD[2][0] == BOARD[1][1] == BOARD[0][2] != "":
        GAME_OVER = True
        return BOARD[1][1]
    if all(BOARD[row][col] != "" for row in range(3) for col in range(3)):
        GAME_OVER = True
        return "Draw"
    return None

def show_game_over_screen(winner):
    end_screen_overlay = pygame.Surface((SCREEN_WIDTH, 200))
    end_screen_overlay.fill(LINE_COLOR)
    SCREEN.blit(end_screen_overlay, (0, SCREEN_HEIGHT - 200))
    if winner == "Draw":
        text = "Draw!"
    else:
        text = f"{winner} Wins!"
    text_surface = FONT.render(text, True, TEXT_COLOR)
    SCREEN.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, SCREEN_HEIGHT - 150))

    # Restart button
    restart_button = pygame.Rect(SCREEN_WIDTH // 4, SCREEN_HEIGHT - 100, SCREEN_WIDTH // 2, 50)
    pygame.draw.rect(SCREEN, BG_COLOR, restart_button)
    button_text = FONT.render("Restart", True, TEXT_COLOR)
    SCREEN.blit(button_text, (SCREEN_WIDTH // 2 - button_text.get_width() // 2, SCREEN_HEIGHT - 95))

def reset_game():
    global BOARD, PLAYER, GAME_OVER
    BOARD = [["" for _ in range(3)] for _ in range(3)]
    PLAYER = "X"
    GAME_OVER = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not GAME_OVER:
            mouseX, mouseY = pygame.mouse.get_pos()
            clicked_row = mouseY // CELL_SIZE
            clicked_col = mouseX // CELL_SIZE
            if BOARD[clicked_row][clicked_col] == "":
                BOARD[clicked_row][clicked_col] = PLAYER
                PLAYER = "O" if PLAYER == "X" else "X"
        if GAME_OVER:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                if SCREEN_WIDTH // 4 <= mouseX <= SCREEN_WIDTH // 4 + SCREEN_WIDTH // 2 and SCREEN_HEIGHT - 100 <= mouseY <= SCREEN_HEIGHT - 50:
                    reset_game()

    SCREEN.fill(BG_COLOR)
    draw_board()
    draw_marks()
    result = check_game_over()
    if GAME_OVER:
        show_game_over_screen(result)

    pygame.display.update()