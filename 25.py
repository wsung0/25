import pygame
from random import *

def setup(level):
    
    global display_time
    display_time = 6 - (level // 3)
    display_time = max(display_time, 1)
    
    shuffle_grid()
    
    
def shuffle_grid():
    
    rows = 5
    columns = 5
    
    cell_size = 130 
    button_size = 110 
    screen_left_margin = 45
    screen_top_margin = 20
    
    grid = [[0 for col in range(columns)] for row in range(rows)]
    
    number = 1 
    while number <= 25:
        row_idx = randrange(0, rows) 
        col_idx = randrange(0, columns) 

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number 
            number += 1

            center_x = screen_left_margin + (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) + (cell_size / 2)

            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)

            number_buttons.append(button)


def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)

    msg = game_font.render(f"{curr_level}", True, ALOHA)
    msg_rect = msg.get_rect(center=start_button.center)
    screen.blit(msg, msg_rect)


def display_game_screen():
    global hidden

    if not hidden:
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        s = display_time
        for i in range(25):
            if elapsed_time > s:
                if len(number_buttons) == i:
                    break
                pygame.draw.rect(screen, WHITE, number_buttons[i])
                s += display_time
                i += 1
            
    for idx, rect in enumerate(number_buttons, start=1):
        idx = 25 - idx + 1
        cell_text = game_font.render(str(idx), True, WHITE)
        text_rect = cell_text.get_rect(center=rect.center)
        screen.blit(cell_text, text_rect)
            
            
def check_buttons(pos):
    global start, start_ticks

    if start:
        check_number_buttons(pos)
    elif start_button.collidepoint(pos):
        start = True
        start_ticks = pygame.time.get_ticks() 


def check_number_buttons(pos):
    global start, hidden, curr_level

    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[-1]:
                del number_buttons[-1]    
            else: 
                game_over()
            break
        
    if len(number_buttons) == 0:
        start = False
        hidden = False
        curr_level += 1
        setup(curr_level)


def game_over():
    global running
    running = False
    
    msg = game_font.render(f"Your level is {curr_level}", True, WHITE)
    msg_rect = msg.get_rect(center=(screen_width/2, screen_height/2))

    screen.fill(BLACK)
    screen.blit(msg, msg_rect)
    
pygame.init()
pygame.font.init()
screen_width = 720 
screen_height = 720 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("25")
game_font = pygame.font.SysFont("arialrounded", 100)

start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

BLACK = (0, 0, 0)  
WHITE = (255, 255, 255)
ALOHA = (244, 201, 107)

number_buttons = [] 
curr_level = 1 
display_time = None 
start_ticks = None 

start = False
hidden = False

setup(curr_level)

# ?????? ??????
running = True 
while running:
    click_pos = None
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False 
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()

    screen.fill(BLACK)

    if start: 
        display_game_screen() 
    else:        
        display_start_screen() 

    if click_pos:
        check_buttons(click_pos)
    pygame.display.update()
    
pygame.time.delay(5000)
pygame.quit()

# https://nadocoding.tistory.com/87 '???????????? ?????????! ?????? ??????'
