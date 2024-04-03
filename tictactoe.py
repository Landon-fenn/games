                                                                                       
import pygame                                                                                        
from pygame.locals import *                                                                                
import random
turn = 0
topL = True
topM = True
topR = True
midL = True
midM = True
midR = True
bottomL = True
bottomM = True
bottomR = True
game_board = [["", "", ""],
               ["", "", ""],
               ["", "", ""]]
win = ""

def end(game_board):
    for x in game_board:
        if x[0] == x[1] == x[2] != "":
            return x[0]
    for y in range(3):
        if game_board[0][y] == game_board[1][y] == game_board[2][y] != "":
            return game_board[0][y]
    if game_board[0][0] == game_board[1][1] == game_board[2][2] != "":
        return game_board[0][0]
    if game_board[0][2] == game_board[1][1] == game_board[2][0] != "":
        return game_board[0][2]
    if "" not in game_board[0] and "" not in game_board[1] and "" not in game_board[2]:
        return "Nobody" 
      


def top_left(mouse_pos):
    global topL
    global turn
    global game_board
    if 100 <= mouse_pos[0] <= 345 and 100 <= mouse_pos[1] <= 345 and topL and playing:
        if turn % 2 == 0:
            pygame.draw.circle(screen, random_color2, [222.5, 222.5], 100, 5)
            game_board[0][0] = "O"
        else:
            pygame.draw.line(screen, random_color3, (222.5-70, 222.5-70), (222.5+70, 222.5+70), 5)
            pygame.draw.line(screen, random_color3, (222.5-70, 222.5+70), (222.5+70, 222.5-70), 5)
            game_board[0][0] = "X"
        topL = False
        turn += 1
def top_mid(mouse_pos):
    global topM
    global turn
    global game_board
    if 355 <= mouse_pos[0] <= 645 and 100 <= mouse_pos[1] <= 345 and topM and playing:
        if turn % 2 == 0:
            pygame.draw.circle(screen, random_color2, [500, 222.5], 100, 5)
            game_board[0][1] = "O"
        else:
            pygame.draw.line(screen, random_color3, (500-70, 222.5-70), (500+70, 222.5+70), 5)
            pygame.draw.line(screen, random_color3, (500-70, 222.5+70), (500+70, 222.5-70), 5)
            game_board[0][1] = "X"
        topM = False
        turn += 1
def top_right(mouse_pos):
    global topR
    global turn
    global game_board
    if 655 <= mouse_pos[0] <= 900 and 100 <= mouse_pos[1] <= 345 and topR and playing:
        if turn % 2 == 0:
            pygame.draw.circle(screen, random_color2, [777.5, 222.5], 100, 5)
            game_board[0][2] = "O"
        else:
            pygame.draw.line(screen, random_color3, (777.5-70, 222.5-70), (777.5+70, 222.5+70), 5)
            pygame.draw.line(screen, random_color3, (777.5-70, 222.5+70), (777.5+70, 222.5-70), 5)
            game_board[0][2] = "X"
        topR = False
        turn += 1
def mid_left(mouse_pos):
    global midL
    global turn
    global game_board
    if 100 <= mouse_pos[0] <= 345 and 355 <= mouse_pos[1] <= 645 and midL and playing:
        if turn % 2 == 0:
            pygame.draw.circle(screen, random_color2, [222.5, 500], 100, 5)
            game_board[1][0] = "O"
        else:
            pygame.draw.line(screen, random_color3, (222.5-70, 500-70), (222.5+70, 500+70), 5)
            pygame.draw.line(screen, random_color3, (222.5-70, 500+70), (222.5+70, 500-70), 5)
            game_board[1][0] = "X"
        midL = False
        turn += 1
def mid_mid(mouse_pos):
    global midM
    global turn
    global game_board
    if 355 <= mouse_pos[0] <= 645 and 355 <= mouse_pos[1] <= 645 and midM and playing:
        if turn % 2 == 0:
            pygame.draw.circle(screen, random_color2, [500, 500], 100, 5)
            game_board[1][1] = "O"
        else:
            pygame.draw.line(screen, random_color3, (500-70, 500-70), (500+70, 500+70), 5)
            pygame.draw.line(screen, random_color3, (500-70, 500+70), (500+70, 500-70), 5)
            game_board[1][1] = "X"
        midM = False
        turn += 1
def mid_right(mouse_pos):
    global midR
    global turn
    global game_board
    if 655 <= mouse_pos[0] <= 900 and 355 <= mouse_pos[1] <= 645 and midR and playing:
        if turn % 2 == 0:
            pygame.draw.circle(screen, random_color2, [777.5, 500], 100, 5)
            game_board[1][2] = "O"
        else:
            pygame.draw.line(screen, random_color3, (777.5-70, 500-70), (777.5+70, 500+70), 5)
            pygame.draw.line(screen, random_color3, (777.5-70, 500+70), (777.5+70, 500-70), 5)
            game_board[1][2] = "X"
        midR = False
        turn += 1
def bottom_left(mouse_pos):
    global bottomL
    global turn
    global game_board
    if 100 <= mouse_pos[0] <= 345 and 655 <= mouse_pos[1] <= 900 and bottomL and playing:
        if turn % 2 == 0:
            pygame.draw.circle(screen, random_color2, [222.5, 777.5], 100, 5)
            game_board[2][0] = "O"
        else:
            pygame.draw.line(screen, random_color3, (222.5-70, 777.5-70), (222.5+70, 777.5+70), 5)
            pygame.draw.line(screen, random_color3, (222.5-70, 777.5+70), (222.5+70, 777.5-70), 5)
            game_board[2][0] = "X"
        bottomL = False
        turn += 1
def bottom_mid(mouse_pos):
    global bottomM
    global turn
    global game_board
    if 355 <= mouse_pos[0] <= 645 and 655 <= mouse_pos[1] <= 900 and bottomM:
        if turn % 2 == 0:
            pygame.draw.circle(screen, random_color2, [500, 777.5], 100, 5)
            game_board[2][1] = "O"
        else:
            pygame.draw.line(screen, random_color3, (500-70, 777.5-70), (500+70, 777.5+70), 5)
            pygame.draw.line(screen, random_color3, (500-70, 777.5+70), (500+70, 777.5-70), 5)
            game_board[2][1] = "X"
        bottomM = False
        turn += 1
def bottom_right(mouse_pos):
    global bottomR
    global turn
    global game_board
    if 655 <= mouse_pos[0] <= 900 and 655 <= mouse_pos[1] <= 900 and bottomR:
        if turn % 2 == 0:
            pygame.draw.circle(screen, random_color2, [777.5, 777.5], 100, 5)
            game_board[2][2] = "O"
        else:
            pygame.draw.line(screen, random_color3, (777.5-70, 777.5-70), (777.5+70, 777.5+70), 5)
            pygame.draw.line(screen, random_color3, (777.5-70, 777.5+70), (777.5+70, 777.5-70), 5)
            game_board[2][2] = "X"
        bottomR = False
        turn += 1

def check(game_board):
    global playing
    


pygame.init()                                                                                                                                                                          

                                                       
screen_width = 1000                                                                                         
screen_height = 1000                                                                                         

font = pygame.font.Font(None, 36)  
playing = True


text_x = 450
text_y = 50

random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
random_color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
random_color3 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

WHITE = (255, 255, 255)                                                                                         
screen = pygame.display.set_mode((screen_width, screen_height))                                                                                         
pygame.display.set_caption('tic tac toes')                                                                                         

run = True                                                                                         
while run:                                                                                         
    for event in pygame.event.get():                                                                                         
        if event.type == pygame.QUIT:                                                                                         
            run = False                                                                                         
        elif event.type == pygame.MOUSEBUTTONDOWN:                                                                                         
            if event.button == 1:  # Left mouse button
                top_left(mouse_pos)
                top_mid(mouse_pos)
                top_right(mouse_pos)
                mid_left(mouse_pos)
                mid_right(mouse_pos)
                mid_mid(mouse_pos)
                bottom_left(mouse_pos)
                bottom_right(mouse_pos)
                bottom_mid(mouse_pos)
                check(game_board)
                win = end(game_board)
                    
                                                                                     
                                                                                         
    text = str(f'{win} is the winner')                                                                                          
    text_surface = font.render(text, True, (255, 255, 255))                                                                                         
    pygame.draw.line(screen, random_color, [350, 100], [350, 900], 5)  #v1                                                        
    pygame.draw.line(screen, random_color, [650, 100], [650, 900], 5)  #v2                                                                                       
    pygame.draw.line(screen, random_color, [100, 350], [900, 350], 5)  #h1                                                                                       
    pygame.draw.line(screen, random_color, [100, 650], [900, 650], 5)  #h2                                                                                       
    mouse_pos = pygame.mouse.get_pos()
    if win == "X" or win == "O" or win == "Nobody":                                                                                       
        screen.blit(text_surface, (text_x, text_y))
        topL, topR, topM = False, False, False
        midL, midR, midM = False, False, False
        bottomL, bottomR, bottomM = False, False, False

     
    pygame.display.flip()