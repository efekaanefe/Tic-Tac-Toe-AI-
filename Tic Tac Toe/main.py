import pygame
from board import TicTacToeBoard
import pygame.font
from AI import *

pygame.font.init()

WIDTH = HEIGHT = 300
SQ_SIZE = WIDTH//3
BLACK = (0,0,0)
WHITE = (255, 255, 255)
FPS = 10
FONT = pygame.font.SysFont("comicsans", 100)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
SCREEN.fill(pygame.Color("white"))

def main():
	board = TicTacToeBoard()
	clock = pygame.time.Clock()

	# You can adjust player vs player, player vs AI 
	# if (x/o)Player = False, AI plays that piece
	# if (x/o)Player = True, Player (usually a person) plays that piece
	xPlayer = True
	oPlayer = False 

	piecePut = True

	while not board.gameover:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				board.gameover = True

			if event.type == pygame.MOUSEBUTTONDOWN:
				if (board.xToMove and xPlayer) or (not board.xToMove and oPlayer):
					x, y = pygame.mouse.get_pos()
					row, col = y//SQ_SIZE, x//SQ_SIZE
					board.putPiece(row, col)
					piecePut = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_z:
					board.undoMove()
					piecePut = True
				

		#AI Movement
		if len(board.moveLog) != 9:
			if (xPlayer == False and board.xToMove) or (oPlayer == False and not board.xToMove):
				row, col = findBestCoordinate(board)
				board.putPiece(row, col)
				#print(board)

		#win/draw condition check and "whose turn" indicator
		if piecePut:
			winCondition = board.checkWinCondition()
			if winCondition == 1:
				print("X WON")
				drawBoardAndGrid(board.board)
				print("RESETING BOARD")
				#pygame.time.delay(1000)
				board.reset()
				#board.gameover = True
			elif winCondition == -1:
				print("O WON")
				drawBoardAndGrid(board.board)
				print("RESETING BOARD")
				#pygame.time.delay(1000)
				board.reset()
				#board.gameover = True
			else: # winCondition == 0
				if board.pieceCount != 9:
					if board.xToMove:
						print("X's turn")
					else:
						print("O's turn")
				else:
					print("Draw")
					print("RESETING BOARD")
					#pygame.time.delay(1000)
					board.reset()

			piecePut = False	
		drawBoardAndGrid(board.board)
	

		
def drawBoardAndGrid(board):
	drawBoard(board)
	drawGrids()
	pygame.display.update()

def drawBoard(board):
	for i in range(3):
		for j in range(3):
			piece = board[i][j]
			if piece != " ":
				text = FONT.render(piece,True ,BLACK)
				x = j*SQ_SIZE + (SQ_SIZE- text.get_width())//2 
				y = i*SQ_SIZE + (SQ_SIZE- text.get_height())//2 
				SCREEN.blit(text, (x, y))
			else:
				x, y = j*SQ_SIZE, i*SQ_SIZE
				rect = pygame.Rect((x, y, SQ_SIZE, SQ_SIZE))
				pygame.draw.rect(SCREEN, WHITE, rect)

def drawGrids():
	for index in range(1, 3):
		line_size = 5 

		# vertical lines
		x_start = index*SQ_SIZE
		y_start = 0
		x_end = index*SQ_SIZE
		y_end = HEIGHT
		pygame.draw.line(SCREEN, BLACK, (x_start, y_start), (x_end, y_end), line_size)

		# horizontal lines
		x_start = 0
		y_start = index*SQ_SIZE
		x_end = WIDTH
		y_end = index*SQ_SIZE
		pygame.draw.line(SCREEN, BLACK, (x_start, y_start), (x_end, y_end), line_size)


	

if __name__ == "__main__":
	main()