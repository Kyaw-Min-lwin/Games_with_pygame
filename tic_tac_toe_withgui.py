import pygame
from math import sqrt

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic-tac-toe')

current_player = 'X'
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
game_going_on = True
winner = None

font = pygame.font.Font('freesansbold.ttf', 42)
ls = []
clock = pygame.time.Clock()


def draw_board():
    pygame.draw.rect(window, (0, 0, 0), (220, 90, 5, 420))
    pygame.draw.rect(window, (0, 0, 0), (380, 90, 5, 420))
    pygame.draw.rect(window, (0, 0, 0), (90, 220, 420, 5))
    pygame.draw.rect(window, (0, 0, 0), (90, 380, 420, 5))
    # pygame.draw.rect(window, (0, 0, 0), (105 + 105 // 2 + 135, 105 + 105 // 2 + 135, 20, 20))


def handle_turn():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


def check_user_input(x, y):
    x_rec = 105 + 105 // 2
    y_rec = 105 + 105 // 2
    r = 60
    for m in range(9):
        if m % 3 == 0 and m != 0:
            x_rec = 105 + 105 // 2
            y_rec += 135
        distance = sqrt((x - x_rec) ** 2 + (y - y_rec) ** 2)
        if distance < r:
            return [x_rec, y_rec, m]
        x_rec += 135


def win():
    global winner
    if check_rows():
        winner = check_rows()
        return True
    elif check_dial():
        winner = check_dial()
        return True
    elif check_col():
        winner = check_col()
        return True
    else:
        winner = None


# Check the rows for a window
def check_rows():
    global game_going_on
    if board[0] == board[1] == board[2] != "-":
        game_going_on = False
        return board[0]
    elif board[3] == board[4] == board[5] != "-":
        game_going_on = False
        return board[3]
    elif board[6] == board[7] == board[8] != "-":
        game_going_on = False
        return board[6]
    else:
        return None


# Check the columns for a window
def check_col():
    global game_going_on
    if board[0] == board[3] == board[6] != "-":
        game_going_on = False
        return board[0]
    elif board[1] == board[4] == board[7] != "-":
        game_going_on = False
        return board[1]
    elif board[2] == board[5] == board[8] != "-":
        game_going_on = False
        return board[2]
    else:
        return None


# Check the diagonals for a window
def check_dial():
    global game_going_on
    if board[0] == board[4] == board[8] != "-":
        game_going_on = False
        return board[0]
    elif board[2] == board[4] == board[6] != "-":
        game_going_on = False
        return board[2]
    else:
        return None


# Check if there is a tie
def tie():
    global game_going_on, winner
    if "-" not in board:
        game_going_on = False
        winner = None
        return True


while game_going_on:
    clock.tick(60)
    window.fill((255, 25, 255))
    draw_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_going_on = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            try:
                x, y, n = check_user_input(*pygame.mouse.get_pos())
                if len(ls) > 0:
                    for i in ls:
                        if x == i[0] and y == i[1]:
                            break
                    else:
                        ls.append([x, y, current_player])
                        board[n] = current_player
                        handle_turn()
                else:
                    board[n] = current_player
                    ls.append([x, y, current_player])
                    handle_turn()
            except TypeError:
                pass

    for i in ls:
        window.blit(font.render(f'{i[2]}', 1, (255, 255, 255)), (i[0], i[1]))

    if win():
        handle_turn()
        pygame.display.update()
        pygame.time.delay(2000)
        window.fill((255, 25, 255))
        window.blit(font.render(f'Player {current_player} won', 1, (0, 0, 0)), (150, 300))
        pygame.display.update()
        pygame.time.delay(2000)
        continue

    if tie():
        pygame.display.update()
        pygame.time.delay(2000)
        window.fill((255, 25, 255))
        window.blit(font.render('It is a draw', 1, (0, 0, 0)), (200, 300))
        pygame.display.update()
        pygame.time.delay(2000)
    pygame.display.update()

print(winner)
