from abc import ABC, abstractmethod
import Math
from enum import ENUM

class Side(ENUM):
	WHITE = 0
	BLACK = 1

class Result(ENUM):
	WIN = 1
	LOSE = 0
	DRAW = .5

class IllegalMove(ENUM):
	SELFCHECK = -1
	AMBIGUOUS = -2
	UNJUMPABLE = -3
	INVALID = -4

class Piece(ABC):
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
		if Math.abs(start[1]-end[1]) == Math.abs(start[0]-end[0]):
			return True
		return False

class King(Piece):
	def canmove(self, start, end):
		super().canmove()
		if Math.abs(start[0]-end[0]) <= 1 and Math.abs(start[0]-end[0]) <= 1:
			return True
		return False


class Bishop(Piece):
	def canmove(self, start, end):
		super().canmove()
		if Math.abs(start[1]-end[1]) == Math.abs(start[0]-end[0]):
			return True
		return False

class Knight(Piece):
	def canmove(self, start, end):
		super().canmove()
		if Math.abs(start[0] - end[0]) == 2 and Math.abs(end[1] - start[1]) == 1:
			return True
		if Math.abs(start[0] - end[0]) == 1 and Math.abs(end[1] - start[1]) == 2:
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
		if Math.abs(start[0] - end[0]) == 1 and (end[1] - start[1]) == 1:
			return True
		return False


class Board:

	def __init__(self):
		self.board = [[0 for i in range(8)] for j in range(8)] # stores pieces in their correct locations
		self.log = [] # stores log of all valid moves

	def legalMove(self, start_pos, end_pos, piece_type):
		# check if piece can legally move toward that position

		# check if pawn is indeed capturing if moving diagonally or on starting pos if moving twice

		# check if moving would place king in check

		# check if move lands in empty square within board limits

		# check if move is blocked by a piece

	def inCheck(self, king):
		# loop through pieces and check if any can capture king

	def createsCheck(self, move, side):
		# check if moving side's piece checks its own king
		# including if king moves into a captureable position


	# takes in Short algebraic notation
	def move(self, move, side):
		# decipher move, including allowing + symbol for checks
		# allowing x symbol to not be included for captures
		# allowing e8(Q) or e8/Q for promotion
		piece_type = 0
		start_pos = 0 # stores board indexes such as (4,3) for e4
		end_pos = 0
		
		# check if it is the correct side's piece
		# checks for ambiguous moves and takes file of departure
		# and rank of departure if necessary i.e. Rdf8 or Qh4e1
		# returns an Illegal for invalid move

		# check for legal move on board

		# make move

		# record in log

		# returns 2 for valid move

		# if game is over, returns a Result

	def printLog(self):
		pass

if __name__ == "__main__":
	pass