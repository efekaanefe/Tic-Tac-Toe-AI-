import random
def findBestCoordinate(boardObject):
	global coordinates, counter
	try:
		coordinates = boardObject.moveLog[-1]
	except IndexError: # if it is first move, corners are best
		corners = [(0,0),(0,2),(2,0),(2,2)]
		coordinates = random.choice(corners)
		return coordinates
	counter = 0
	findMoveMinMax(boardObject)
	print("AI looked for " + str(counter) + " many moves")
	return coordinates




def findMoveMinMax(boardObject, firstCall = True):

	global coordinates, counter
	counter += 1
	b = boardObject
	winCondition = b.checkWinCondition()
	if winCondition != 0 or len(b.moveLog) == 9:
		return winCondition

	# X maximizes
	# O minimizes
	if b.xToMove:
		maxScore = -1
		for i in range(3):
			for j in range(3):
				piece = b.board[i][j]
				if piece == " ":
					b.putPiece(i, j)
					score = findMoveMinMax(b, False)
					if score > maxScore:
						maxScore = score
						if firstCall:
							coordinates = (i, j)
					b.undoMove()
					if maxScore == 1:
						return maxScore

		return maxScore

	else:
		minScore = 1
		for i in range(3):
			for j in range(3):
				piece = b.board[i][j]
				if piece == " ":
					b.putPiece(i, j)
					score = findMoveMinMax(b, False)
					if score < minScore:
						minScore = score
						if firstCall: 
							coordinates = (i, j)
					b.undoMove()
					if minScore == -1:
						return minScore

		return minScore