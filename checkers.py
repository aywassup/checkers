class CheckerBoard:
	#similar to chess A1 A2 B3 ...
	def __init__(self):
		self.setupBoard()
		self.turn = False
	def skip(self, start_location):
		start_row = ord(start_location[0]) - ord("a")
		start_column = int(start_location[1]) - 1
		cont = input("Do you want to skip your turn?")
		if cont == "yes":
			pass
		else:
			self.turn = not self.turn
	def validMove(self, start_location, end_location, debug=False):
		if len(start_location) > 2 or len(end_location) > 2:
			return False
		start_row = ord(start_location[0]) - ord("a")
		start_column = int(start_location[1]) - 1
		end_row = ord(end_location[0]) - ord("a")
		end_column = int(end_location[1]) - 1
		print(start_row, start_column, end_row, end_column)
		letter = self.board[start_row][start_column]
		if debug:
			print(start_row)
			print(start_column)
		if start_row > 7 or start_row < 0:
			print("out of range")
			return False
		if end_row > 7 or end_row < 0:
			print("out of range")
			return False
		if start_column > 7 or start_column < 0:
			print("out of range")
			return False
		if end_column > 7 or end_column < 0:
			print("out of range")
			return False
		if not self._isSpaceEmpty(end_row, end_column):
			return False
		if (self.board[start_row][start_column] == "x" and self.turn == True) or (self.board[start_row][start_column] == "o" and self.turn == False):
			return False
		if letter == "x":
			if not (start_row - end_row == 1 and abs(start_column - end_column) == 1):
				if start_row - end_row == 2 and abs(start_column - end_column) == 2:
					if self.board[end_row + 1][(start_column+end_column)//2].lower() == "o":
						self.board[end_row + 1][(start_column+end_column)//2] = " "
						self.skip(start_location)
					else:
						return False
		if letter == "X":
			if not (abs(start_row - end_row == 1) and abs(start_column - end_column) == 1):
				if abs(start_row - end_row) == 2 and abs(start_column - end_column) == 2:
					if self.board[(start_row+end_row)//2][(start_column+end_column)//2].lower() == "o":
						self.board[(start_row+end_row)//2][(start_column+end_column)//2] = " "
						self.skip(start_location)
					else:
						return False
		if letter == "o":
			if not (start_row - end_row == -1 and abs(start_column - end_column) == 1):
				if start_row - end_row == -2 and abs(start_column - end_column) == 2:
					if self.board[end_row - 1][(start_column+end_column)//2].lower() == "x":
						self.board[end_row - 1][(start_column+end_column)//2] = " "
						self.skip(start_location)
					else:
						return False
		if letter == "O":
			if not (abs(start_row - end_row == 1) and abs(start_column - end_column) == 1):
				if abs(start_row - end_row) == 2 and abs(start_column - end_column) == 2:
					if self.board[(start_row+end_row)//2][(start_column+end_column)//2].lower() == "x":
						self.board[(start_row+end_row)//2][(start_column+end_column)//2] = " "
						self.skip(start_location)
					else:
						return False
				else:
					return False
		if end_row == 7 and letter == "o":
			self.board[end_row][end_column] = "O"
		if end_row == 0 and letter == "x":
			self.board[end_row][end_column] = "X"
		else:
			self.board[end_row][end_column] = letter
		self.turn = not self.turn
		self.board[start_row][start_column] = " "

		"""
		if == x then start row - end row = 1 and abs(column - end-column) == 1

		if == o then start row - end row = -1 and abs(column - end-column) == 1
		"""
		return True	
	def playerMove(self, start_location, end_location, debug=False):
		letter = self.board[start_row][start_column]
		if validMove(start_location, end_location, debug=False) == True:
			self.board[start_row][start_column] = " "
			self.board[end_row][end_column] = letter

	def _isSpaceEmpty(self, r, c):
		return self.board[r][c] == " "

	def setupBoard(self):
		self.board = []
		#here we make the board 8 by 8
		for i in range(8):
			l = []
			for j in range(8):
				l.append(" ")
			self.board.append(l)

		count = 0 #for i in self.board: 
		self.place_piece_on_row(self.board[0], "o", 0) 
		self.place_piece_on_row(self.board[1], "o", 1)
		self.place_piece_on_row(self.board[2], "o", 0)
		self.place_piece_on_row(self.board[5], "x", 1)
		self.place_piece_on_row(self.board[6], "x", 0)
		self.place_piece_on_row(self.board[7], "x", 1)

	def place_piece_on_row(self, row, x, start_location): 
		count = 0 
		for i in row: 
			if (count + start_location) % 2 == 0: 
				row[count] = x 
			count += 1
	def maketurn(self): 
		pass 
	#how do i detect clicks in cmd? 
	def printBoard(self): 
		print("   ",str(1) + "   ", str(2) + "   ", str(3) + "   ", str(4) + "   ", str(5) + "   ", str(6) + "   ", str(7) + "    ", str(8) + "   ") 
		count = 0 
		for i in self.board: 
			print(chr(ord("A") + count), i) 
			count += 1 
	def playerWin(self): 
		count_x = 0 
		count_o = 0 
		for row in self.board: 
			for i in row: 
				if i == "x": 
					count_x += 1 
				if i == "o": 
					count_o += 1
		if count_x == 0: 
			return True 
		if count_o == 0: 
			return True 
		else: 
			return False

player = CheckerBoard()
player.printBoard()
while player.playerWin() == False:
	starting = input("What is the starting place?")
	ending = input("What is the ending place?")
	print(player.validMove(starting, ending, debug=True))
	player.printBoard()


