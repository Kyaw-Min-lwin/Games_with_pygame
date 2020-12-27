import pygame
import random
import time
import math

pygame.init()
win = pygame.display.set_mode((700, 550))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
img_ls = [pygame.image.load('images/hangman' + str(i) + '.png') for i in range(7)]
font = pygame.font.Font('freesansbold.ttf', 28)
letters = []
ls_of_pos = []
usr_inpt_ls_of_correct_values = []
guesses = []
radius = 20
y = 440
increment = 0
no_of_circles = 0
for i in range(26):
    if no_of_circles == 13:
        y = 500
        increment = 0
    letters.append([50 + increment, y, chr(65 + i), True])
    increment += 50
    no_of_circles += 1


# selecting a random word from a text file
def get_word():
    with open('word_list.txt', 'r') as f:
        ls = (f.readlines())
    word = random.choice(ls).strip()
    return word


random_word = get_word()
length = len(random_word)
print(random_word)
list_of_dash = []
x = 350


def draw_dash():
    x = 350
    global guesses
    guesses = ['-' for _ in range(length)]
    pos_of_x = {0: x}
    index = 1
    # draw the dashes
    for i in range(length):
        list_of_dash.append(pygame.draw.rect(win, (0, 0, 0), (x, 100, 20, 5)))
        x += 25
        pos_of_x[index] = x
        index += 1

    for i in usr_inpt_ls_of_correct_values:
        if i[1] not in list_of_dash:
            list_of_dash[i[0]] = win.blit(font.render(i[1], True, (0, 0, 0)), (pos_of_x[i[0]], 69))
            guesses[i[0]] = i[1]

    return list_of_dash


def display_image_ofthething():
    global run
    # check the score n display the correct image
    if check == 0:
        win.blit(img_ls[0], (100, 50))
    elif check == 1:
        win.blit(img_ls[1], (100, 50))
    elif check == 2:
        win.blit(img_ls[2], (100, 50))
    elif check == 3:
        win.blit(img_ls[3], (100, 50))
    elif check == 4:
        win.blit(img_ls[4], (100, 50))
    elif check == 5:
        win.blit(img_ls[5], (100, 50))
    else:
        win.blit(img_ls[6], (100, 50))
        pygame.display.update()
        time.sleep(2)
        win.fill(WHITE)
        win.blit(font.render('You lose', True, (0, 0, 0)), (250, 250))
        win.blit(font.render(f'The word was {random_word}', True, (0, 0, 0)), (180, 280))
        pygame.display.update()
        time.sleep(2)
        run = False


def draw_letters():
    global ls_of_pos
    # draw the circle
    ls_of_pos = []
    # drawing the circles
    for i in letters:
        x_of_circle, y_of_circle, letter, visible = i
        if visible:
            pygame.draw.circle(win, BLACK, (x_of_circle, y_of_circle), radius, 3)
            win.blit(font.render(letter, 1, BLACK), (x_of_circle - 11, y_of_circle - 12))


check = 0
run = True

while run:
    pygame.time.delay(100)
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for j, i in enumerate(letters):
                x, y, letter, visible = i
                if visible:
                    distance = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                    if distance < radius:
                        letters[j][3] = False
                        usr_input = letters[j][2].lower()
                        if usr_input in random_word:
                            for word in enumerate(random_word):
                                if word[1] == usr_input:
                                    usr_inpt_ls_of_correct_values.append(word)
                        else:
                            check += 1

    win.fill(WHITE)

    # draw the dashes and the alphabets
    draw_letters()
    draw_dash()
    # for the wooden img
    display_image_ofthething()
    if ''.join(guesses) == random_word:
        win.fill(WHITE)
        win.blit(font.render(f'The word is {random_word}', True, (0, 0, 0)), (200, 220))
        win.blit(font.render(f'You Win', True, (0, 0, 0)), (260, 250))
        run = False
        pygame.display.update()
        time.sleep(2)

    pygame.display.update()

pygame.quit()
