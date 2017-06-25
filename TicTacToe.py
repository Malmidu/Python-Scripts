import random
boardMarkers = ['1', '2', '3', '4', '5', '6','7', '8', '9']
boardState = """\n%s|%s|%s
-----
%s|%s|%s
-----
%s|%s|%s \n""" % (boardMarkers[0], boardMarkers[1], boardMarkers[2], boardMarkers[3], boardMarkers[4], boardMarkers[5], boardMarkers[6], boardMarkers[7], boardMarkers[8])

def boardUpdate():
	global boardState
	boardState = """\n%s|%s|%s
-----
%s|%s|%s
-----
%s|%s|%s \n""" % (boardMarkers[0], boardMarkers[1], boardMarkers[2], boardMarkers[3], boardMarkers[4], boardMarkers[5], boardMarkers[6], boardMarkers[7], boardMarkers[8])
	print boardState


def checkBoard():
	global boardMarkers
	gameOver = False
	count = 0
	if boardMarkers[0] == boardMarkers[1] and boardMarkers[0] == boardMarkers[2]:
		gameOver = True
	elif boardMarkers[3] == boardMarkers[4] and boardMarkers[4] == boardMarkers[5]:
		gameOver = True
	elif boardMarkers[6] == boardMarkers[8] and boardMarkers[7] == boardMarkers[8]:
		gameOver = True
	elif boardMarkers[0] == boardMarkers[3] and boardMarkers[0] == boardMarkers[6]:
		gameOver = True
	elif boardMarkers[1] == boardMarkers[4] and boardMarkers[1] == boardMarkers[7]:
		gameOver = True
	elif boardMarkers[2] == boardMarkers[5] and boardMarkers[2] == boardMarkers[8]:
		gameOver = True
	elif boardMarkers[0] == boardMarkers[4] and boardMarkers[4] == boardMarkers[8]:
		gameOver = True
	elif boardMarkers[2] == boardMarkers[4] and boardMarkers[4] == boardMarkers[6]:
		gameOver = True
	
	for i in boardMarkers:
		if i == "X" or i == "O":
			count += 1

	if count == 9:
		gameOver = True
			
	return gameOver

def checkState():
	global boardMarkers
	xVals = []
	oVals = []
	for i, x in enumerate(boardMarkers):
		if x == 'X':
			xVals.append(i)
	for i, x in enumerate(boardMarkers):
		if x == 'O':
			oVals.append(i)
	return (xVals, oVals)

def comTurn():

	global boardMarkers
	global boardState
	Move = 0
	VicCheck = False
	DefCheck = False
	(xVals, oVals) = checkState()
	while Move == 0:
		for i in [0,3,6]:
			if boardMarkers[i] == boardMarkers[i+1]:
				if boardMarkers[i] == 'X':
					if boardMarkers[i+2] != 'O' and boardMarkers[i+2] != 'X':
						Move = (i+3)
						return Move
				elif VicCheck == True:
					if boardMarkers[i+2] != 'O' and boardMarkers[i+2] != 'X':
						Move = (i+3)
						return Move
						
			elif boardMarkers[i] == boardMarkers[i+2]:
				if boardMarkers[i] == 'X':
					if boardMarkers[i+1] != 'O' and boardMarkers[i+1] != 'X':
						Move = (i+2)
						return Move
				elif VicCheck == True:
					if boardMarkers[i+1] != 'O' and boardMarkers[i+1] != 'X':
						Move = (i+2)
						return Move	
						
		for i in [0, 1, 2]:
			if boardMarkers[i] == boardMarkers[i+3]:
				if boardMarkers[i] == 'X':
					if boardMarkers[i+6] != 'O' and boardMarkers[i+6] != 'X':
						Move = (i+7)
						print Move
						return Move
				elif VicCheck == True:
					if boardMarkers[i+6] != 'O' and boardMarkers[i+6] != 'X':
						Move = (i+7)
						return Move
						
			elif boardMarkers[i] == boardMarkers[i+6]:
				if boardMarkers[i] == 'X':
					if boardMarkers[i+3] != 'O' and boardMarkers[i+3] != 'X':
						Move = (i+4)
						print Move
						return Move
				elif VicCheck == True:
					if boardMarkers[i+3] != 'O' and boardMarkers[i+3] != 'X':
						Move = (i+4)
						return Move
						
		for i in [6, 7, 8]:
			if boardMarkers[i] == boardMarkers[i-3]:
				if boardMarkers[i] == 'X':
					if boardMarkers[i-6] != 'O' and boardMarkers[i-6] != 'X':
						Move = (i-5)
						return Move
				elif VicCheck == True:
					if boardMarkers[i-6] != 'O' and boardMarkers[i-6] != 'X':
						Move = (i-5)
						return Move
			
			elif boardMarkers[i] == boardMarkers[i-6]:
				if boardMarkers[i] == 'X':
					if boardMarkers[i-3] != 'O' and boardMarkers[i-3] != 'X':
						Move = (i-2)
						return Move
				elif VicCheck == True:
					if boardMarkers[i-3] != 'O' and boardMarkers[i-3] != 'X':
						Move = (i-2)
						return Move
						
		for i in [2, 5, 8]:
			if boardMarkers[i] == boardMarkers[i-1]:
				if boardMarkers[i] == "X":
					if boardMarkers[i-2] != 'O' and boardMarkers[i-2] != 'X':
						Move = (i-1)
						return Move
				elif VicCheck == True:
					if boardMarkers[i-2] != 'O' and boardMarkers[i-2] != 'X':
						Move = (i-1)
						return Move
						
			elif boardMarkers[i] == boardMarkers[i-2]:
				if boardMarkers[i] == "X":
					if boardMarkers[i-1] != 'O' and boardMarkers[i-1] != 'X':
						Move = (i)
						return Move
				elif VicCheck == True:
					if boardMarkers[i-1] != 'O' and boardMarkers[i-1] != 'X':
						Move = (i)
						return Move
						
		if boardMarkers[4] == boardMarkers[2]:
			if boardMarkers[4] == "X":
				if boardMarkers[6] != 'O' and boardMarkers[6] != 'X':
					Move = 7
					return Move
			elif VicCheck == True:
				if boardMarkers[6] != 'O' and boardMarkers[6] != 'X':
					Move = 7
					return Move
					
		elif boardMarkers[4] == boardMarkers[0]:
			if boardMarkers[4] == "X":
				if boardMarkers[8] != 'O' and boardMarkers[8] != 'X':
					Move = 9
					return Move
			elif VicCheck == True:
				if boardMarkers[8] != 'O' and boardMarkers[8] != 'X':
					Move = 9
					return Move
					
		elif boardMarkers[4] == boardMarkers[8]:
			if boardMarkers[4] == "X":
				if boardMarkers[0] != "O" and boardMarkers[0] != "X":
					Move = 1
					return Move
			elif VicCheck == True:
				if boardMarkers[0] != "O" and boardMarkers[0] != "X":
					Move = 1
					return Move
		
		elif boardMarkers[4] == boardMarkers[6]:
			if boardMarkers[4] == "X":
				if boardMarkers[2] != "O" and boardMarkers[2] != "X":
					Move = 3
					return Move
			elif VicCheck == True:
				if boardMarkers[2] != "O" and boardMarkers[2] != "X":
					Move = 3
					return Move
		
		
		if VicCheck == True:
			DefCheck = True
		
		if DefCheck == True:
		
			crossCount = 0
			cross = [1, 3, 5, 7]
			corner = [0, 2, 6, 8]
			Total = [0, 1, 2, 3, 5, 6, 7, 8]
			if boardMarkers[4] != "O" and boardMarkers[4] != "X":
				Move = 5
				return Move
			
			for i in [1, 3, 5, 7]:
				if boardMarkers[i] == "X":
					crossCount += 1
			
			if boardMarkers[4] == "X" and crossCount < 1:
				
				for i in cross:
					if boardMarkers[i] == "O" or boardMarkers[i] == "X":
						cross.remove(i)
				print cross
				moveChoice = random.choice(cross)	
				Move = moveChoice + 1
				return Move
				
			elif boardMarkers[4] == "X" and crossCount >= 1:
				
				for i in [1, 3, 5, 7]:
					if boardMarkers[i] == "X":
						if boardMarkers[i+1] != "O" and boardMarkers[i+1] != "X" and boardMarkers[i-1] != "O" and boardMarkers[i-1] != "X":
							coin = random.randrange(0, 3, 2)
							Move = i + coin
							return Move
						
							
						elif boardMarkers[i+1] != "O" and boardMarkers[i+1] != "X":
							Move = (i+2)
							return Move
						elif boardMarkers[i-1] != "O" and boardMarkers[i-1] != "X":
							Move = i
							return Move
				for i in cross:
					if boardMarkers[i] == "O" or boardMarkers[i] == "X":
						cross.remove(i)
				print cross
				moveChoice = random.choice(cross)	
				Move = moveChoice + 1
				return Move
					
			for i in Total:
					if boardMarkers[i] == "O" or boardMarkers[i] == "X":
						Total.remove(i)
			print Total
			moveChoice = random.choice(Total)
			Move = (moveChoice + 1)
			return Move
				
				
		VicCheck = True
			
		
	
def main():
	global boardMarkers
	global boardState
	gameOver = False
	print boardState
	while True:
		playerTurn = True
		while playerTurn == True:
			playerSquare = input("Select the number of the square you want to choose: ")
			i = int(playerSquare) - 1
			if boardMarkers[i] != 'O' and boardMarkers[i] != 'X':
				boardMarkers[i] = 'O'
				boardUpdate()
				playerTurn = False
			else:
				print "That space is already taken, please choose another \n"
		if checkBoard():
			print "Game Over!\n"
			exit()
		print "Computer Turn... \n"
		
		Move = comTurn()
		
		boardMarkers[Move - 1] = 'X'
		boardUpdate()
			
		if checkBoard():
			print "Game Over!\n"
			exit()
		
	
	
if __name__ == "__main__":
	main()