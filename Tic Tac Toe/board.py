class TicTacToeBoard: # "X"/"O"/" "
	def __init__(self):
		self.board = [
					[" ", " ", " "],
					[" ", " ", " "],
					[" ", " ", " "]]

		self.pieceCount = 0
		self.xToMove = True
		self.moveLog = []
		self.gameover = False


	def putPiece(self, row, col):
		if self.board[row][col] == " ":
			if self.xToMove:
				self.board[row][col] = "X"
			else:
				self.board[row][col] = "O"
			self.xToMove = not self.xToMove
			self.pieceCount += 1
			self.moveLog += [(row, col)]
			return True
		else:
			print("you should put the piece on empty space")
			return False



	def undoMove(self):
		if len(self.moveLog) != 0:
			row, col = self.moveLog[-1]
			self.board[row][col] = " "
			self.moveLog.pop()
			self.gameover = False
			self.pieceCount -= 1
			self.xToMove = not self.xToMove

	def reset(self):
		self.board = [
					[" ", " ", " "],
					[" ", " ", " "],
					[" ", " ", " "]]

		self.pieceCount = 0
		self.xToMove = True
		self.moveLog = []
	""" 
	 1 = X wins
	 -1 = O wins
	 0 = not finished or draw
	"""
	def checkWinCondition(self):
		#diagonal from (0,0) to (2,2)
		diagonal1 = [self.board[0][0], self.board[1][1], self.board[2][2]]
		#diagonal from (0,2) to (2,0)
		diagonal2 = [self.board[0][2], self.board[1][1], self.board[2][0]]

		if diagonal1.count("X") == 3 or diagonal2.count("X") == 3:
			return 1
		elif diagonal1.count("O") == 3 or diagonal2.count("O") == 3:
			return -1
			
		for i in range(3):
			#row-wise
			row = self.board[i]
			#col-wise
			col = [self.board[0][i], self.board[1][i], self.board[2][i]]
			
			if row.count("X") == 3 or col.count("X") == 3:
				return 1
			elif row.count("O") == 3 or col.count("O") == 3:
				return -1

		return 0

	def __repr__(self):
		visible_board = ""
		for i in range(3):
			for j in range(3):
				visible_board += self.board[i][j]
				if j != 2:
					visible_board += "|"
			if i != 2:
				visible_board += "\n" + "-"*5 + "\n"

		return visible_board

