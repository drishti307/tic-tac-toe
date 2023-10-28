import pygame, sys
import numpy as np
import util
import pandas as pands 

pygame.init()

WIDTH=600
HEIGHT=700
BDR=3
BDC=3
BGC=(28,170,156)
WHITE= (255,255,255)
BLACK=(0,0,0)
GREY=(232,232,232)
LINE_COLOR = (23, 145, 135)
CIR_RAD=50
CIR_WD=12
CIR_CLR=BLACK
CRS_CLR=WHITE
CRS_WD=28
SPACE=55
SQ_SIZE=200
LINE_WIDTH = 8
WIN_LINE_WIDTH = 10
# x ----->
# y increases downwards

def draw_line():
    pygame.draw.line(screen, LINE_COLOR, (0,200), (600, 200), 6)
    pygame.draw.line(screen, LINE_COLOR, (0,400), (600, 400), 6)

    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), 6)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), 6)


def is_avail(row,col):
    return board[row][col]==0

def mark_square( row, col, player):
    board[row][col]=player

def is_board_full (BDR, BDC):
    for ro in range(BDR):
        for co in range(BDC):
            if board[ro][co]==0:
                return False
    return True

def draw_fig():
    for ro in range(BDR):
        for co in range(BDC):
            if board[ro][co]==1:
                pygame.draw.circle(screen, CIR_CLR, (int(co*SQ_SIZE + 100), int(ro*SQ_SIZE + 100)), CIR_RAD, CIR_WD)
            elif board[ro][co]==2:
                pygame.draw.line(screen, CRS_CLR, (co*SQ_SIZE +SPACE, ro*200 +200 - SPACE), (co*200+200 - SPACE, ro*200 + SPACE), CRS_WD)
                pygame.draw.line(screen, CRS_CLR, (co*SQ_SIZE +SPACE, ro*200 + SPACE), (co*200+200 - SPACE, ro*200 + 200-SPACE), CRS_WD)



def check_win(player):
	# vertical win check
	for col in range(BDC):
		if board[0][col] == player and board[1][col] == player and board[2][col] == player:
			draw_vertical_winning_line(col, player)
			return True

	# horizontal win check
	for row in range(BDR):
		if board[row][0] == player and board[row][1] == player and board[row][2] == player:
			draw_horizontal_winning_line(row, player)
			return True

	# asc diagonal win check
	if board[2][0] == player and board[1][1] == player and board[0][2] == player:
		draw_asc_diagonal(player)
		return True

	# desc diagonal win chek
	if board[0][0] == player and board[1][1] == player and board[2][2] == player:
		draw_desc_diagonal(player)
		return True

	return False

def draw_vertical_winning_line(col, player):
	posX = col * SQ_SIZE + SQ_SIZE//2

	if player == 1:
		color = CIR_CLR
	elif player == 2:
		color = GREY

	pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH )

def draw_horizontal_winning_line(row, player):
	posY = row * SQ_SIZE + SQ_SIZE//2

	if player == 1:
		color = CIR_CLR
	elif player == 2:
		color = GREY

	pygame.draw.line( screen, color, (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH )

def draw_asc_diagonal(player):
	if player == 1:
		color = CIR_CLR
	elif player == 2:
		color = GREY

	pygame.draw.line( screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH )

def draw_desc_diagonal(player):
	if player == 1:
		color = CIR_CLR
	elif player == 2:
		color = GREY

	pygame.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH )

def restart():
	screen.fill(BGC)
	draw_line()
	player=1
	for row in range(BDR):
		for col in range(BDC):
			board[row][col] = 0


screen = pygame.display.set_mode((WIDTH,HEIGHT))  #(wxh)
pygame.display.set_caption("Sudoku, Tic Tac Toe!")
screen.fill(BGC)

board=np.zeros((BDR, BDC))
print(board)   

draw_line()
player=1
game_over=False
#main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Close button works
            sys.exit()
        
        if event.type== pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX=event.pos[0]
            mouseY=event.pos[1]

            clk_row=mouseY//200
            clk_col=mouseX//200

            if is_avail(clk_row, clk_col):
                    mark_square(clk_row, clk_col, player)
                    if check_win(player):
                        game_over=True

                    player=player%2+1
                    draw_fig()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player=1
                game_over=False

    
    
    pygame.display.update()

