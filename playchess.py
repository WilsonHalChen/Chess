from abc import ABC, abstractmethod
from enum import Enum

class Side(Enum):
	WHITE = 0
	BLACK = 1

class Result(Enum):
	WIN = 1
	LOSE = 0
	DRAW = .5

class IllegalMove(Enum):
	SELFCHECK = -1
	AMBIGUOUS = -2
	UNJUMPABLE = -3
	INVALID = -4

# Pieces
class Piece(ABC):
	def __init__(self, side):
		self.side = side

	@abstractmethod
	def canmove(self):
		if start == end:
			return False

class Queen(Piece):
	def canmove(self, start, end):
		super().canmove()
		if start[0] == end[0]:
			return True
		if start[1] == end[1]:
			return True
		if abs(start[1]-end[1]) == abs(start[0]-end[0]):
			return True
		return False

class King(Piece):
	def canmove(self, start, end):
		super().canmove()
		if abs(start[0]-end[0]) <= 1 and abs(start[0]-end[0]) <= 1:
			return True
		return False


class Bishop(Piece):
	def canmove(self, start, end):
		super().canmove()
		if abs(start[1]-end[1]) == abs(start[0]-end[0]):
			return True
		return False

class Knight(Piece):
	def canmove(self, start, end):
		super().canmove()
		if abs(start[0] - end[0]) == 2 and abs(end[1] - start[1]) == 1:
			return True
		if abs(start[0] - end[0]) == 1 and abs(end[1] - start[1]) == 2:
			return True
		return False

class Rook(Piece):
	def canmove(self, start, end):
		super().canmove()
		if start[0] == end[0]:
			return True
		if start[1] == end[1]:
			return True
		return False

class Pawn(Piece):
	def canmove(self, start, end):
		super().canmove()
		if start[0] == end[0] and (end[1] - start[1]) in (1,2):
			return True
		if abs(start[0] - end[0]) == 1 and (end[1] - start[1]) == 1:
			return True
		return False


class Board:
	col_index_convert = ['a','b','c','d','e','f','g','h']

	def __init__(self, fen=None):
		self.log = [] # stores log of all valid moves
		self.board = [[0 for i in range(8)] for j in range(8)] # stores pieces by (col, row) as strs
		self.enpassant = '-'
		self.half_moves = 0 # after 50 halfmoves by each player, game draws
		self.castle_rights = "KQkq" # Uppercase denotes White rights, '-' denotes no castling
		self.turn = 'w'
		if fen is not None:
			# import FEN Chess Notation
			fields = fen.split()
			pieces = fields[0].split("/")
			for row in pieces:
				col = 0
				for ch in row:
					if ch.isnumeric():
						col += int(ch)
					else:
						self.board[col][row] = ch
				col += 1
			self.turn = fields[1]
			self.castle_rights = fields[2]
			en_passant_targets = fields[3].lower()
			if en_passant_targets != '-':
				self.enpassant = (col_index_convert.index(en_passant_targets[0]), en_passant_targets[1])
			self.half_moves = fields[4]
		else:
			# init start board
			for j in range(len(self.board[0])):
				self.board[j][1] = "P"
				self.board[j][6] = "p"
				if j == 0 or j == 7:
					self.board[j][0] = "R"
					self.board[j][7] = "r"
				if j == 1 or j == 6:
					self.board[j][0] = "N"
					self.board[j][7] = "n"
				if j == 2 or j == 5:
					self.board[j][0] = "B"
					self.board[j][7] = "b"
				if j == 3:
					self.board[j][0] = "Q"
					self.board[j][7] = "q"
				if j == 4:
					self.board[j][0] = "K"
					self.board[j][7] = "k"




	def legalMove(self, start_pos, end_pos, piece_type):
		# check if piece can legally move toward that position

		# check if pawn is indeed capturing if moving diagonally or on starting pos if moving twice

		# check if moving would place king in check

		# check if move lands in empty square within board limits

		# check if move is blocked by a piece
		pass

	def inCheck(self, king):
		# loop through pieces and check if any can capture king
		pass

	def createsCheck(self, move, side):
		# check if moving side's piece checks its own king
		# including if king moves into a captureable position
		pass

	def decipher(self, move):
		pass

	# takes in Short algebraic notation
	def move(self, move, side):
		# decipher move, including allowing + symbol for checks
		# x symbol for captures
		# = for draw or end game
		piece_type = 0
		start_pos = 0 # stores board indexes such as (4,3) for e4
		end_pos = 0
		promoted_piece = 0
		capture_flag = 0
		double_pawn = 0
		en_passant = 0
		castling = 0
		
		# check for castling rights
		# get rid of old en passants and add new en passant if double move pawn
		# check if it is the correct side's piece
		# checks for ambiguous moves and takes file of departure
		# and rank of departure if necessary i.e. Rdf8 or Qh4e1
		# returns an Illegal for invalid move

		# check for legal move on board

		# make move

		# record in log

		# returns 2 for valid move

		# if game is over, returns a Result
		# make sure to check for halfmove clock for Draws
		pass

	def export(self):
		# Prints log out in PGN format
		pass

	def printLog(self):
		pass

	def printBoard(self):
		for i in range(len(self.board)-1, -1, -1):
			for j in range(len(self.board[0])):
				print(self.board[j][i], end=' ')
			print()

if __name__ == "__main__":
	# Asks for move 
	# keeps track of side to move
	# can import and export boards
	# can end and begin games
	game = Board()
	game.printBoard()