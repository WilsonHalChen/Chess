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
	major_pieces = {"K", "Q", "N", "B", "R"}
	blank_space = '-' # this defines empty space on the board

	def __init__(self, fen=None):
		self.log = [] # stores log of all valid moves
		self.board = [[self.blank_space for i in range(8)] for j in range(8)] # stores pieces by (col, row) as strs
		self.enpassant = '-'
		self.half_moves = 0 # after 50 halfmoves by each player, game draws
		self.castle_rights = "KQkq" # Uppercase denotes White rights, '-' denotes no castling
		self.turn = 'w'
		if fen is not None:
			# TODO Fix FEN Import
			# import FEN Chess Notation
			fields = fen.split()
			lines = fields[0].split("/")
			for i in range(len(lines)):
				row = (len(self.board) - 1) - i
				col = 0
				for ch in lines:
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

	def inBounds(self, square):
		return (0 < square[0] < len(self.board)) and (0 < square[1] < len(self.board))

	def contains(self, square, piece):
		return self.board[square[0]][square[1]] == piece


	def legalMove(self, start_pos, end_pos, piece_type):
		# check if piece can legally move toward that position

		# check if pawn is indeed capturing if moving diagonally or on starting pos if moving twice

		# check if moving would place king in check

		# check if move lands in empty square within board limits

		# check if move is blocked by a piece
		pass

	def inCheck(self, board, side):
		# locate king position
		to_locate = ''
		enemy_pieces = ['Q','K','N','B','R']
		if side == Side.WHITE:
			to_locate = 'K'
			enemy_pieces = [x.lower() for x in enemy_pieces]
		if side == Side.BLACK:
			to_locate = 'k'

		king = ''
		print("To locate: {}".format(to_locate))
		for i in range(len(board)):
			for j in range(len(board)):
				if board[i][j] == to_locate:
					king = (i,j)

		# check if pawns can capture king
		if side == Side.WHITE:
			print("Printing king: {}".format(king))
			sq_1 = (king[0]+1, king[1]+1)
			sq_2 = (king[0]-1, king[1]+1)
			if (self.inBounds(sq_1) and self.contains(sq_1, enemy_piece)) or (self.inBounds(sq_2) and self.contains(sq_2, enemy_piece)):
				return True
		if side == Side.BLACK:
			sq_1 = (king[0]+1, king[1]-1)
			sq_2 = (king[0]-1, king[1]-1)
			if (self.inBounds(sq_1) and self.contains(sq_1, enemy_piece)) or (self.inBounds(sq_2) and self.contains(sq_2, enemy_piece)):
				return True

		# check if any piece can move into king's position
		# move like knight
		enemy_piece = enemy_pieces[2]
		knight_moves = [(king[0]+1, king[1]+2), (king[0]+1, king[1]-2), (king[0]-1, king[1]+2), (king[0]-1, king[1]+2),
						(king[0]+2, king[1]+1), (king[0]+2, king[1]-1), (king[0]-2, king[1]+1), (king[0]-2, king[1]+1)]
		for sq in knight_moves:
			if (0 < sq[0] < 7) and (0 < sq[1] < 7) and board[sq[0]][sq[1]] == enemy_piece:
				return True

		# move like king
		enemy_piece = enemy_pieces[1]
		king_moves = [(king[0], king[1]+1), (king[0], king[1]-1), (king[0]+1, king[1]), (king[0]+1, king[1]+1),
					(king[0]+1, king[1]-1), (king[0]-1, king[1]), (king[0]-1, king[1]+1), (king[0]-1, king[1]-1)]
		for sq in king_moves:
			if (0 < sq[0] < 7) and (0 < sq[1] < 7) and board[sq[0]][sq[1]] == enemy_piece:
				return True

		# move like bishop
		enemy_piece = (enemy_pieces[0], enemy_pieces[3])
		increment_i = 1
		increment_j = 1
		temp_pos = (king[0] + increment_i, king[1] + increment_j)
		while (0 < temp_pos[0] < 7) and (0 < temp_pos[1] < 7):
			if temp_pos != self.blank_space:
				if board[temp_pos[0]][temp_pos[1]] in enemy_piece:
					return True
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)

		increment_i = -1
		increment_j = 1
		temp_pos = (king[0] + increment_i, king[1] + increment_j)
		while (0 < temp_pos[0] < 7) and (0 < temp_pos[1] < 7):
			if temp_pos != self.blank_space:
				if board[temp_pos[0]][temp_pos[1]] in enemy_piece:
					return True
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)

		increment_i = 1
		increment_j = -1
		temp_pos = (king[0] + increment_i, king[1] + increment_j)
		while (0 < temp_pos[0] < 7) and (0 < temp_pos[1] < 7):
			if temp_pos != self.blank_space:
				if board[temp_pos[0]][temp_pos[1]] in enemy_piece:
					return True
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)

		increment_i = -1
		increment_j = -1
		temp_pos = (king[0] + increment_i, king[1] + increment_j)
		while (0 < temp_pos[0] < 7) and (0 < temp_pos[1] < 7):
			if temp_pos != self.blank_space:
				if board[temp_pos[0]][temp_pos[1]] in enemy_piece:
					return True
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)


		# move like rook
		enemy_piece = (enemy_pieces[0], enemy_pieces[4])
		increment_i = 1
		increment_j = 0
		temp_pos = (king[0] + increment_i, king[1] + increment_j)
		while (0 < temp_pos[0] < 7) and (0 < temp_pos[1] < 7):
			if temp_pos != self.blank_space:
				if board[temp_pos[0]][temp_pos[1]] in enemy_piece:
					return True
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)

		increment_i = 0
		increment_j = 1
		temp_pos = (king[0] + increment_i, king[1] + increment_j)
		while (0 < temp_pos[0] < 7) and (0 < temp_pos[1] < 7):
			if temp_pos != self.blank_space:
				if board[temp_pos[0]][temp_pos[1]] in enemy_piece:
					return True
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)

		increment_i = -1
		increment_j = 0
		temp_pos = (king[0] + increment_i, king[1] + increment_j)
		while (0 < temp_pos[0] < 7) and (0 < temp_pos[1] < 7):
			if temp_pos != self.blank_space:
				if board[temp_pos[0]][temp_pos[1]] in enemy_piece:
					return True
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)

		increment_i = 0
		increment_j = -1
		temp_pos = (king[0] + increment_i, king[1] + increment_j)
		while (0 < temp_pos[0] < 7) and (0 < temp_pos[1] < 7):
			if temp_pos != self.blank_space:
				if board[temp_pos[0]][temp_pos[1]] in enemy_piece:
					return True
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)

		return False

	def createsCheck(self, move, side):
		# check if moving side's piece checks its own king
		# including if king moves into a captureable position
		pass

	def decipher(self, move, side):
		piece_type = -1
		start_pos = -1 # stores board indexes such as (4,3) for e4
		end_pos = -1
		promoted_piece = -1
		capture_flag = False
		double_pawn = False
		en_passant = -1

		# Check for Pawn move
		# set capture if contains 'x'

		# For pawn move, set piece type 
		# find end pos, and which pawn can move to it
		# check for en passant flag
		# check for promotion
		# check for double pawn move

		# For major piece move,
		# Get piece type
		# find end pos, check if it is a capture
		# 
		return (piece_type, start_pos, end_pos, promoted_piece, capture_flag, double_pawn, en_passant)

	# takes in Short algebraic notation
	def move(self, move, side):
		move = move.strip()
		# decipher move, including allowing + symbol for checks
		# x symbol for captures
		# = for draw or end game

		# Check for castle
		if move == "0-0" or move == "O-O":
			# does king have castling rights?
			# Are pieces out of the way?
			# does move through check?
			pass

		if move == "0-0-0" or move == "O-O-O":
			pass

		decoded_move = self.decipher(move, side)
		# Return values for decipher()
		piece_type = decoded_move[0]
		start_pos = decoded_move[1] # stores board indexes such as (4,3) for e4
		end_pos = decoded_move[2]
		promoted_piece = decoded_move[3]
		capture_flag = decoded_move[4]
		double_pawn = decoded_move[5]
		en_passant = decoded_move[6]
		castling = decoded_move[7]
		
		# check for castling rights
		# get rid of old en passants and add new en passant if double move pawn
		# check if it is the correct side's piece
		# checks for ambiguous moves and takes file of departure
		# and rank of departure if necessary i.e. Rdf8 or Qh4e1
		# returns an Illegal for invalid move

		# check for legal move on board

		# make move and update previous space as self.blank_space
		# update halfmove clock
		# update active color

		# record in log

		# returns 2 for valid move

		# if game is over, returns a Result
		# make sure to check for halfmove clock for Draws
		pass

	def export(self, path):
		# Prints log out in PGN format to file
		print("Printing to {}".format(path))
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
	game = Board("rnbqkbnr/pppp2pp/5p2/4p2Q/4P3/2N5/PPPP1PPP/R1B1KBNR b KQkq - 1 3")
	game.printBoard()
	print(game.inCheck(game.board, Side.WHITE))