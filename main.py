import pygame
from Pieces import Piece
from Player import Player
import math

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Checkers")
FPS_CAP = 60

# Board For Drawing The Red And Black Squares
BOARD = [[0, 1, 0, 1, 0, 1, 0, 1],
		 [1, 0, 1, 0, 1, 0, 1, 0],
		 [0, 1, 0, 1, 0, 1, 0, 1],
		 [1, 0, 1, 0, 1, 0, 1, 0],
		 [0, 1, 0, 1, 0, 1, 0, 1],
		 [1, 0, 1, 0, 1, 0, 1, 0],
		 [0, 1, 0, 1, 0, 1, 0, 1],
		 [1, 0, 1, 0, 1, 0, 1, 0]]

#Board To Keep a Track of the Pieces
pieces_board = [[0, 2, 0, 2, 0, 2, 0, 2],
		 		[2, 0, 2, 0, 2, 0, 2, 0],
		 		[0, 2, 0, 2, 0, 2, 0, 2],
		 		[0, 0, 0, 0, 0, 0, 0, 0],
		 		[0, 0, 0, 0, 0, 0, 0, 0],
		 		[1, 0, 1, 0, 1, 0, 1, 0],
		 		[0, 1, 0, 1, 0, 1, 0, 1],
		 		[1, 0, 1, 0, 1, 0, 1, 0]]



# Counts the no. of pieces of a player
def count_pieces(board, number):
	count = 0
	for y in board:
		for x in y:
			if x == number:
				count += 1
	return count

#Finds Distance between 2 Points
def distance_formula(tuple1, tuple2):
	dist = math.sqrt(((tuple2[0] - tuple1[0]) ** 2) + ((tuple2[1] - tuple1[1]) ** 2))
	return dist



SQR_LEN = 75


BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

#Initializing Player Class
player1 = Player(RED, [Piece(BLACK, False, i, False) for i in range(count_pieces(pieces_board, 1))])
player2 = Player(WHITE, [Piece(WHITE, False, i, False) for i in range(count_pieces(pieces_board, 2))])


p1i = 0
p2j = 0
player1Pieces = player1.getPieces()
player2Pieces = player2.getPieces()

#Sets the 1 in The piece board to player 1's pieces and 2 to player 2's pieces
tempy_coord = 0
for y in pieces_board:
	tempx_coord = 0
	for x in y:
		if x == 2:
			pieces_board[tempy_coord][tempx_coord] = player2Pieces[p2j]
			p2j += 1
		elif x == 1:
			pieces_board[tempy_coord][tempx_coord] = player1Pieces[p1i]
			p1i += 1
		tempx_coord += 1
	tempy_coord += 1

# Gets the row and col of a piece based on its position on the screen
def getPieceCoords(piece):
	piececol = (piece.getCenter()[0] - round(SQR_LEN/2)) // SQR_LEN
	piecerow = (piece.getCenter()[1] - round(SQR_LEN/2)) // SQR_LEN
	return (piecerow, piececol)

# Moves the piece and captures a piece when possible
def Move(piecerow, piececol, row, col):
	if row > -1 and col > -1:
		if piecerow - 2 == row and piececol - 2 == col:
			if turn == "up":
				player1.removePiece(pieces_board[piecerow-1][piececol-1])
			elif turn == 'down':
				player2.removePiece(pieces_board[piecerow-1][piececol-1])
			pieces_board[piecerow-1][piececol-1] = 0
		elif piecerow - 2 == row and piececol + 2 == col:
			if turn == "up":
				player1.removePiece(pieces_board[piecerow-1][piececol+1])
			elif turn == 'down':
				player2.removePiece(pieces_board[piecerow-1][piececol+1])
			pieces_board[piecerow-1][piececol+1] = 0
		elif piecerow + 2 == row and piececol + 2 == col:
			if turn == "up":
				player1.removePiece(pieces_board[piecerow+1][piececol+1])
			elif turn == 'down':
				player2.removePiece(pieces_board[piecerow+1][piececol+1])
			pieces_board[piecerow+1][piececol+1] = 0
		elif piecerow + 2 == row and piececol - 2 == col:
			if turn == "up":
				player1.removePiece(pieces_board[piecerow+1][piececol-1])
			elif turn == 'down':
				player2.removePiece(pieces_board[piecerow+1][piececol-1])
			pieces_board[piecerow+1][piececol-1] = 0

		if row == 0 or row == 7:
			pieces_board[piecerow][piececol].setKing()
		pieces_board[piecerow][piececol], pieces_board[row][col] = pieces_board[row][col], pieces_board[piecerow][piececol]


# Gets the Possible moves of a piece
def getMoves(piecerow, piececol, turn):
	fin_list = [] # List for all possible moves of the piece
	if turn == "down": # If Player1 Turn
		if pieces_board[piecerow][piececol].getKing(): # If the Piece is king
			if pieces_board[piecerow+1][piececol-1] in player2.getPieces() or  pieces_board[piecerow+1][piececol+1] in player2.getPieces(): # If diagonal down left or right pieces are pieces of other player
				if (piecerow+2 <= 7 and piececol-2 >= 0): # Check to make sure it isn't out of index
					if pieces_board[piecerow+2][piececol-2] == 0 and pieces_board[piecerow+1][piececol-1] in player2.getPieces(): # For down-left
						fin_list.append((piecerow+2, piececol-2))
				if piecerow+2 <= 7 and piececol + 2 <= 7: # Make sure it isnt out of index
					if pieces_board[piecerow+2][piececol+2] == 0 and pieces_board[piecerow+1][piececol+1] in player2.getPieces(): # For down-right
						fin_list.append((piecerow+2, piececol+2))
			if pieces_board[piecerow-1][piececol-1] in player2.getPieces() or  pieces_board[piecerow-1][piececol+1] in player2.getPieces(): # If diagonal up left or right pieces are pieces of other player
				if (piecerow-2 >= 0 and piececol-2 >= 0): # Check if index isn't out of range
					if pieces_board[piecerow-2][piececol-2] == 0 and pieces_board[piecerow-1][piececol-1] in player2.getPieces(): # For up-left
						fin_list.append((piecerow-2, piececol-2))
				if piecerow-2 >= 0 and piececol + 2 <= 7: # Check if index isn't out of range
					if pieces_board[piecerow-2][piececol+2] == 0 and pieces_board[piecerow-1][piececol-1] in player2.getPieces(): # For up-right
						fin_list.append((piecerow-2, piececol+2))
		else: # If not King
			if pieces_board[piecerow-1][piececol-1] in player2.getPieces() or  pieces_board[piecerow-1][piececol+1] in player2.getPieces(): # If diagonal up left or right pieces are pieces of other player
				if (piecerow-2 >= 0 and piececol-2 >= 0): # Check if index isn't out of range
					if pieces_board[piecerow-2][piececol-2] == 0 and pieces_board[piecerow-1][piececol-1] in player2.getPieces(): # For up-left
						fin_list.append((piecerow-2, piececol-2))
				if piecerow-2 >= 0 and piececol + 2 <= 7: # Check if index isn't out of range
					if pieces_board[piecerow-2][piececol+2] == 0 and pieces_board[piecerow-1][piececol+1] in player2.getPieces(): # For up-right
						fin_list.append((piecerow-2, piececol+2))
			if len(fin_list) > 0: # If something is appended then return the list
				return fin_list
		# Moves which doesn't involve Capturing other pieces
		if (piecerow-1 >= 0 and piececol-1 >= 0): # Check if index not out of range
			if pieces_board[piecerow-1][piececol-1] == 0: # top-left
				fin_list.append((piecerow-1, piececol-1))
		if (piecerow-1 >= 0 and piececol+1 <= 7): # Check if index not out of range
			if pieces_board[piecerow-1][piececol+1] == 0: # top-right
				fin_list.append((piecerow-1, piececol+1))
	else: # Player2 turn
		if pieces_board[piecerow][piececol].getKing(): # If piece is king
			if pieces_board[piecerow-1][piececol-1] in player1.getPieces() or  pieces_board[piecerow-1][piececol+1] in player1.getPieces(): # Checks for top-left and top-right for player1 pieces
				if (piecerow-2 >= 0 and piececol-2 >= 0):
					if pieces_board[piecerow-2][piececol-2] == 0 and pieces_board[piecerow-1][piececol-1] in player1.getPieces(): # up-left
						fin_list.append((piecerow-2, piececol-2))
				if piecerow-2 >= 0 and piececol + 2 <= 7:
					if pieces_board[piecerow-2][piececol+2] == 0 and pieces_board[piecero-1][piececol+1] in player1.getPieces(): # up-right
						fin_list.append((piecerow-2, piececol+2))

			if pieces_board[piecerow+1][piececol-1] in player1.getPieces() or  pieces_board[piecerow+1][piececol+1] in player1.getPieces(): # Checks for down-left or down-right
				if (piecerow+2 <= 7 and piececol-2 >= 0):
					if pieces_board[piecerow+2][piececol-2] == 0 and pieces_board[piecerow+1][piececol-1] in player1.getPieces(): # down-left
						fin_list.append((piecerow+2, piececol-2))
				if piecerow+2 <= 7 and piececol + 2 <= 7:
					if pieces_board[piecerow+2][piececol+2] == 0 and pieces_board[piecerow+1][piececol+1] in player1.getPieces(): # down-right
						fin_list.append((piecerow+2, piececol+2))
			if len(fin_list) > 0:
				return fin_list
		else: # If piece is not king
			if pieces_board[piecerow+1][piececol-1] in player1.getPieces() or  pieces_board[piecerow+1][piececol+1] in player1.getPieces(): # Checking down-left and down-right
				if (piecerow+2 <= 7 and piececol-2 >= 0):
					if pieces_board[piecerow+2][piececol-2] == 0 and pieces_board[piecerow+1][piececol-1] in player1.getPieces(): # down-left
						fin_list.append((piecerow+2, piececol-2))
				if piecerow+2 <= 7 and piececol+2 <= 7:
					if pieces_board[piecerow+2][piececol+2] == 0 and pieces_board[piecerow+1][piececol+1] in player1.getPieces(): # down-right
						fin_list.append((piecerow+2, piececol+2))
			if len(fin_list) > 0:
				return fin_list
		if (piecerow+1 <= 7 and piececol-1 >= 0): # Movements not involving capturing a piece
			if pieces_board[piecerow+1][piececol-1] == 0: # down-left
				fin_list.append((piecerow+1, piececol-1))
		if (piecerow+1 <= 7 and piececol+1 <= 7):
			if pieces_board[piecerow+1][piececol+1] == 0: # down-right
				fin_list.append((piecerow+1, piececol+1))
	return fin_list

# Resets all pieces to not selected and sets the piece given as arguement to selected
def resetIsSelected(piecerow, piececol):
	for i in player1.getPieces():
		i.setSelected(False)
	for i in player2.getPieces():
		i.setSelected(False)
	turn_dict[turn].getPieces()[turn_dict[turn].getPieces().index(pieces_board[piecerow][piececol])].setSelected(True)

# Main thing that draws stuff
def gamedraw():

	#Draws the red and black square with board
	y_coord = 0
	for y in BOARD:
		x_coord = 0
		for x in y:
			if x == 0:
				pygame.draw.rect(WIN, BLACK, pygame.Rect(x_coord*SQR_LEN, y_coord*SQR_LEN, SQR_LEN, SQR_LEN))
			elif x == 1:
				pygame.draw.rect(WIN, RED, pygame.Rect(x_coord*SQR_LEN, y_coord*SQR_LEN, SQR_LEN, SQR_LEN))
			x_coord += 1
		y_coord += 1

	# Draws the pieces
	y_coord2 = 0
	for y in pieces_board:
		x_coord2 = 0
		for x in y:
			if x != 0:
				x.drawSelf(WIN, ((x_coord2*SQR_LEN) + round(SQR_LEN/2), (y_coord2*SQR_LEN) + round(SQR_LEN/2)))
			x_coord2 += 1
		y_coord2 += 1

	# Shows Possible moves of a piece when it is selected
	for i in turn_dict[turn].getPieces():
		if i.getSelected():
			pieceCoords = getPieceCoords(i)
			moves = getMoves(pieceCoords[0], pieceCoords[1], turn)
			for coords in moves:
				pygame.draw.circle(WIN, BLUE, ((coords[1] * SQR_LEN) + round(SQR_LEN/2), (coords[0] * SQR_LEN) + round(SQR_LEN/2)), 15)



	pygame.display.update()

def main():
	run = True
	global turn_dict
	global turn
	turn = "down"
	turn_dict = {
		"down": player1,
		"up": player2
	}

	clock = pygame.time.Clock()

	while run:
		clock.tick(FPS_CAP)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				mousepos = pygame.mouse.get_pos()
				for i in turn_dict[turn].getPieces():    # turn_dict[turn] gives the players whose turn it is currently
					if i.getSelected(): # If any piece is selected
					 	# Gets the square which is clicked
						pressedCol = mousepos[0] // SQR_LEN
						pressedRow = mousepos[1] // SQR_LEN
						pieceCoords = getPieceCoords(i)
						moves = getMoves(pieceCoords[0], pieceCoords[1], turn)
						if (pressedRow, pressedCol) in moves: # If the pressed square is one of the possible moves
							Move(pieceCoords[0], pieceCoords[1], pressedRow, pressedCol)
							# Sets the turn to opposite Player
							if turn == "down":
								turn = "up"
							else:
								turn = "down"
					if distance_formula(mousepos, i.getCenter()) < i.radius: # If the distance between a piece and the clicked
						pieceCoords = getPieceCoords(i) # square is less than its radius i.e mouse is clicked within the pieces
						resetIsSelected(pieceCoords[0], pieceCoords[1])
						break

		gamedraw()

	pygame.quit()

main()
