class Piece:
	pass

class Queen(Piece):
	pass

class King(Piece):
	pass

class Bishop(Piece):
	pass

class Knight(Piece):
	pass

class Rook(Piece):
	pass

class Queen(Piece):
	pass

class Board:

	def __init__(self):
		self.board = [[0 for i in range(8)] for j in range(8)] # stores pieces in their correct locations
		self.log = [] # stores log of all valid moves

	# takes in Short algebraic notation
	def move(self, notation):
		# decipher move, including allowing + symbol for checks
		# allowing x symbol to not be included for captures
		# allowing e8(Q) or e8/Q for promotion
		# checks for ambiguous moves and takes file of departure
		# and rank of departure if necessary i.e. Rdf8 or Qh4e1
		# returns error value for invalid move
		piece_type = 0
		start_pos = 0
		end_pos = 0
		# check if piece can legally move toward that position

		# check if moving would place king in check

		# check if move lands in empty square


if __name__ == "__main__":
	pass