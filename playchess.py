from abc import ABC, abstractmethod
from enum import Enum

class Side(Enum):
	def __str__(self):
		return str(self.value)

	WHITE = 'w'
	BLACK = 'b'

class Result(Enum):
	WIN = 1
	LOSE = 0
	DRAW = .5

class AmbiguousMove(Exception):
	pass

class InvalidMove(Exception):
	pass

# Pieces
class Piece(ABC):
	@abstractmethod
	def canmove(self):
		if start == end:
			return False

	@staticmethod
	@abstractmethod
	def canCapture(board, side, target):
		# returns all pieces of my type and side that can capture target
		pass

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

	@staticmethod
	def canCapture(board, side, target):
		enemy_pieces = ['Q','K','N','B','R','P']
		if side == Side.BLACK:
			enemy_pieces = [x.lower() for x in enemy_pieces]
		result = []
		enemy_piece = enemy_pieces[0]
		increment_i = 1
		increment_j = 1
		temp_pos = (target[0]+increment_i, target[1]+increment_j)
		while (0 <= temp_pos[0] < len(board) and 0 <= temp_pos[1] < len(board)):
			temp_sq = board[temp_pos[0]][temp_pos[1]]
			if temp_sq != '-':
				if temp_sq in enemy_piece:
					result.append(temp_pos)
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)
			

		increment_i = -1
		increment_j = 1
		temp_pos = (target[0]+increment_i, target[1]+increment_j)
		while (0 <= temp_pos[0] < len(board) and 0 <= temp_pos[1] < len(board)):
			temp_sq = board[temp_pos[0]][temp_pos[1]]
			if temp_sq != '-':
				if temp_sq in enemy_piece:
					result.append(temp_pos)
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)
			

		increment_i = 1
		increment_j = -1
		temp_pos = (target[0]+increment_i, target[1]+increment_j)
		while (0 <= temp_pos[0] < len(board) and 0 <= temp_pos[1] < len(board)):
			temp_sq = board[temp_pos[0]][temp_pos[1]]
			if temp_sq != '-':
				if temp_sq in enemy_piece:
					result.append(temp_pos)
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)
			

		increment_i = -1
		increment_j = -1
		temp_pos = (target[0]+increment_i, target[1]+increment_j)
		while (0 <= temp_pos[0] < len(board) and 0 <= temp_pos[1] < len(board)):
			temp_sq = board[temp_pos[0]][temp_pos[1]]
			if temp_sq != '-':
				if temp_sq in enemy_piece:
					result.append(temp_pos)
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)
			


		# move like rook
		increment_i = 1
		increment_j = 0
		temp_pos = (target[0]+increment_i, target[1]+increment_j)
		while (0 <= temp_pos[0] < len(board) and 0 <= temp_pos[1] < len(board)):
			if board[temp_pos[0]][temp_pos[1]] != '-':
				if board[temp_pos[0]][temp_pos[1]] in enemy_piece:
					result.append(temp_pos)
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)
			

		increment_i = 0
		increment_j = 1
		temp_pos = (target[0]+increment_i, target[1]+increment_j)
		while (0 <= temp_pos[0] < len(board) and 0 <= temp_pos[1] < len(board)):
			if board[temp_pos[0]][temp_pos[1]] != '-':
				if board[temp_pos[0]][temp_pos[1]] in enemy_piece:
					result.append(temp_pos)
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)
			

		increment_i = -1
		increment_j = 0
		temp_pos = (target[0]+increment_i, target[1]+increment_j)
		while (0 <= temp_pos[0] < len(board) and 0 <= temp_pos[1] < len(board)):
			if board[temp_pos[0]][temp_pos[1]] != '-':
				if board[temp_pos[0]][temp_pos[1]] in enemy_piece:
					result.append(temp_pos)
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)
			

		increment_i = 0
		increment_j = -1
		temp_pos = (target[0]+increment_i, target[1]+increment_j)
		while (0 <= temp_pos[0] < len(board) and 0 <= temp_pos[1] < len(board)):
			if board[temp_pos[0]][temp_pos[1]] != '-':
				if board[temp_pos[0]][temp_pos[1]] in enemy_piece:
					result.append(temp_pos)
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)

		return result

class King(Piece):
	def canmove(self, start, end):
		super().canmove()
		if abs(start[0]-end[0]) <= 1 and abs(start[0]-end[0]) <= 1:
			return True
		return False

	@staticmethod
	def canCapture(board, side, target):
		enemy_pieces = ['Q','K','N','B','R','P']
		if side == Side.BLACK:
			enemy_pieces = [x.lower() for x in enemy_pieces]
		result = []
		enemy_piece = enemy_pieces[1]
		king_moves = [(target[0], target[1]+1), (target[0], target[1]-1), (target[0]+1, target[1]), (target[0]+1, target[1]+1),
					(target[0]+1, target[1]-1), (target[0]-1, target[1]), (target[0]-1, target[1]+1), (target[0]-1, target[1]-1)]
		for sq in king_moves:
			if (0 <= sq[0] < len(board) and 0 <= sq[1] < len(board)) and board[sq[0]][sq[1]] == enemy_piece:
				result.append(sq)

		return result


class Bishop(Piece):
	def canmove(self, start, end):
		super().canmove()
		if abs(start[1]-end[1]) == abs(start[0]-end[0]):
			return True
		return False

	@staticmethod
	def canCapture(board, side, target):
		enemy_pieces = ['Q','K','N','B','R','P']
		if side == Side.BLACK:
			enemy_pieces = [x.lower() for x in enemy_pieces]
		result = []
		enemy_piece = enemy_pieces[3]
		increment_i = 1
		increment_j = 1
		temp_pos = (target[0]+increment_i, target[1]+increment_j)
		while (0 <= temp_pos[0] < len(board) and 0 <= temp_pos[1] < len(board)):
			temp_sq = board[temp_pos[0]][temp_pos[1]]
			if temp_sq != '-':
				if temp_sq in enemy_piece:
					result.append(temp_pos)
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)
			

		increment_i = -1
		increment_j = 1
		temp_pos = (target[0]+increment_i, target[1]+increment_j)
		while (0 <= temp_pos[0] < len(board) and 0 <= temp_pos[1] < len(board)):
			temp_sq = board[temp_pos[0]][temp_pos[1]]
			if temp_sq != '-':
				if temp_sq in enemy_piece:
					result.append(temp_pos)
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)
			

		increment_i = 1
		increment_j = -1
		temp_pos = (target[0]+increment_i, target[1]+increment_j)
		while (0 <= temp_pos[0] < len(board) and 0 <= temp_pos[1] < len(board)):
			temp_sq = board[temp_pos[0]][temp_pos[1]]
			if temp_sq != '-':
				if temp_sq in enemy_piece:
					result.append(temp_pos)
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)
			

		increment_i = -1
		increment_j = -1
		temp_pos = (target[0]+increment_i, target[1]+increment_j)
		while (0 <= temp_pos[0] < len(board) and 0 <= temp_pos[1] < len(board)):
			temp_sq = board[temp_pos[0]][temp_pos[1]]
			if temp_sq != '-':
				if temp_sq in enemy_piece:
					result.append(temp_pos)
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)

		return result

class Knight(Piece):
	def canmove(self, start, end):
		super().canmove()
		if abs(start[0] - end[0]) == 2 and abs(end[1] - start[1]) == 1:
			return True
		if abs(start[0] - end[0]) == 1 and abs(end[1] - start[1]) == 2:
			return True
		return False

	@staticmethod
	def canCapture(board, side, target):
		enemy_pieces = ['Q','K','N','B','R','P']
		if side == Side.BLACK:
			enemy_pieces = [x.lower() for x in enemy_pieces]
		result = []
		enemy_piece = enemy_pieces[2]
		knight_moves = [(target[0]+1, target[1]+2), (target[0]+1, target[1]-2), (target[0]-1, target[1]+2), (target[0]-1, target[1]-2),
						(target[0]+2, target[1]+1), (target[0]+2, target[1]-1), (target[0]-2, target[1]+1), (target[0]-2, target[1]-1)]
		for sq in knight_moves:
			if (0 <= sq[0] < len(board) and 0 <= sq[1] < len(board)) and board[sq[0]][sq[1]] == enemy_piece:
				result.append(sq)

		return result

class Rook(Piece):
	def canmove(self, start, end):
		super().canmove()
		if start[0] == end[0]:
			return True
		if start[1] == end[1]:
			return True
		return False

	@staticmethod
	def canCapture(board, side, target):
		enemy_pieces = ['Q','K','N','B','R','P']
		if side == Side.BLACK:
			enemy_pieces = [x.lower() for x in enemy_pieces]
		result = []
		enemy_piece = enemy_pieces[4]
		increment_i = 1
		increment_j = 0
		temp_pos = (target[0]+increment_i, target[1]+increment_j)
		while (0 <= temp_pos[0] < len(board) and 0 <= temp_pos[1] < len(board)):
			if board[temp_pos[0]][temp_pos[1]] != '-':
				if board[temp_pos[0]][temp_pos[1]] in enemy_piece:
					result.append(temp_pos)
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)
			

		increment_i = 0
		increment_j = 1
		temp_pos = (target[0]+increment_i, target[1]+increment_j)
		while (0 <= temp_pos[0] < len(board) and 0 <= temp_pos[1] < len(board)):
			if board[temp_pos[0]][temp_pos[1]] != '-':
				if board[temp_pos[0]][temp_pos[1]] in enemy_piece:
					result.append(temp_pos)
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)
			

		increment_i = -1
		increment_j = 0
		temp_pos = (target[0]+increment_i, target[1]+increment_j)
		while (0 <= temp_pos[0] < len(board) and 0 <= temp_pos[1] < len(board)):
			if board[temp_pos[0]][temp_pos[1]] != '-':
				if board[temp_pos[0]][temp_pos[1]] in enemy_piece:
					result.append(temp_pos)
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)
			

		increment_i = 0
		increment_j = -1
		temp_pos = (target[0]+increment_i, target[1]+increment_j)
		while (0 <= temp_pos[0] < len(board) and 0 <= temp_pos[1] < len(board)):
			if board[temp_pos[0]][temp_pos[1]] != '-':
				if board[temp_pos[0]][temp_pos[1]] in enemy_piece:
					result.append(temp_pos)
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)

		return result

class Pawn(Piece):
	def canmove(self, start, end):
		super().canmove()
		if start[0] == end[0] and (end[1] - start[1]) in (1,2):
			return True
		if abs(start[0] - end[0]) == 1 and (end[1] - start[1]) == 1:
			return True
		return False

	@staticmethod
	def canCapture(board, side, target):
		enemy_pieces = ['Q','K','N','B','R','P']
		if side == Side.BLACK:
			enemy_pieces = [x.lower() for x in enemy_pieces]
		result = []
		enemy_piece = enemy_pieces[5]
		if side == Side.WHITE:
			sq_1 = (target[0]+1, target[1]+1)
			sq_2 = (target[0]-1, target[1]+1)
			if (0 <= sq_1[0] < len(board) and 0 <= sq_1[1] < len(board) and board[sq_1[0]][sq_1[1]] == enemy_piece):
				result.append(sq_1)
			if (0 <= sq_2[0] < len(board) and 0 <= sq_2[0] < len(board) and board[sq_2[0]][sq_2[1]] == enemy_piece):
				result.append(sq_2)
		if side == Side.BLACK:
			sq_1 = (target[0]+1, target[1]-1)
			sq_2 = (target[0]-1, target[1]-1)
			if (0 <= sq_1[0] < len(board) and 0 <= sq_1[1] < len(board) and board[sq_1[0]][sq_1[1]] == enemy_piece):
				result.append(sq_1)
			if (0 <= sq_2[0] < len(board) and 0 <= sq_2[1] < len(board) and board[sq_2[0]][sq_2[1]] == enemy_piece):
				result.append(sq_2)

		return result

getObject = {'Q':Queen,
			'K':King,
			'B':Bishop,
			'N':Knight,
			'R':Rook}

class Board:
	col_index_convert = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
	num_to_alpha = {val: key for key, val in col_index_convert.items()}
	major_pieces = {"K", "Q", "N", "B", "R"}
	blank_space = '-' # this defines empty space on the board

	def __init__(self, fen=None):
		# TODO store initial FEN
		self.log = [] # stores FEN of every board state
		self.board = [[self.blank_space for i in range(8)] for j in range(8)] # stores pieces by (col, row) as strs
		self.turn = Side.WHITE
		self.castle_rights = "KQkq" # Uppercase denotes White rights, '-' denotes no castling
		self.enpassant = '-' # stores in internal (x,y) notation by ints
		self.half_moves = 0 # after 50 halfmoves by each player, game draws
		self.full_moves = 0
		if fen is not None:
			self.log.append(fen)
			# import FEN Chess Notation
			fields = fen.split()
			lines = fields[0].split("/")
			for i in range(len(lines)):
				row = (len(self.board) - 1) - i
				col = 0
				for ch in lines[i]:
					if ch.isnumeric():
						# print("Incrementing col {} by {}".format(col, ch))
						col += int(ch)
					else:
						# print("Assigning {} to ({},{})".format(ch, col, row))
						self.board[col][row] = ch
						col += 1
			self.turn = Side(fields[1])
			self.castle_rights = fields[2]
			en_passant_targets = fields[3].lower()
			if en_passant_targets != '-':
				self.enpassant = (self.col_index_convert[en_passant_targets[0]], en_passant_targets[1]-1)
			self.half_moves = int(fields[4])
			self.full_moves = int(fields[5])
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

	# TODO (OPTIONAL) Move to_locate to separate sub function (used also in immovableking)
	def inCheck(self, board, side):
		# determines if side's king can be captured
		# locate king position
		to_locate = ''
		enemy_pieces = ['Q','K','N','B','R','P']
		if side == Side.WHITE:
			to_locate = 'K'
			enemy_pieces = [x.lower() for x in enemy_pieces]
		if side == Side.BLACK:
			to_locate = 'k'

		king = ''
		# print("To locate: {}".format(to_locate))
		for i in range(len(board)):
			for j in range(len(board)):
				if board[i][j] == to_locate:
					king = (i,j)

		# print("Printing king: {}".format(king))
		# check if any piece can move into king's position

		# check if pawns can capture king
		enemy_piece = enemy_pieces[5]
		if side == Side.WHITE:
			sq_1 = (king[0]+1, king[1]+1)
			sq_2 = (king[0]-1, king[1]+1)
			if (self.inBounds(sq_1) and self.contains(sq_1, enemy_piece)) or (self.inBounds(sq_2) and self.contains(sq_2, enemy_piece)):
				return True
		if side == Side.BLACK:
			sq_1 = (king[0]+1, king[1]-1)
			sq_2 = (king[0]-1, king[1]-1)
			if (self.inBounds(sq_1) and self.contains(sq_1, enemy_piece)) or (self.inBounds(sq_2) and self.contains(sq_2, enemy_piece)):
				return True

		# move like knight
		enemy_piece = enemy_pieces[2]
		knight_moves = [(king[0]+1, king[1]+2), (king[0]+1, king[1]-2), (king[0]-1, king[1]+2), (king[0]-1, king[1]+2),
						(king[0]+2, king[1]+1), (king[0]+2, king[1]-1), (king[0]-2, king[1]+1), (king[0]-2, king[1]+1)]
		for sq in knight_moves:
			if self.inBounds(sq) and self.contains(sq, enemy_piece):
				return True

		# move like king
		enemy_piece = enemy_pieces[1]
		king_moves = [(king[0], king[1]+1), (king[0], king[1]-1), (king[0]+1, king[1]), (king[0]+1, king[1]+1),
					(king[0]+1, king[1]-1), (king[0]-1, king[1]), (king[0]-1, king[1]+1), (king[0]-1, king[1]-1)]
		for sq in king_moves:
			if self.inBounds(sq) and self.contains(sq, enemy_piece):
				return True

		# move like bishop
		enemy_piece = (enemy_pieces[0], enemy_pieces[3])
		increment_i = 1
		increment_j = 1
		temp_pos = (king[0]+increment_i, king[1]+increment_j)
		while self.inBounds(temp_pos):
			temp_sq = board[temp_pos[0]][temp_pos[1]]
			if temp_sq != self.blank_space:
				if temp_sq in enemy_piece:
					return True
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)
			

		increment_i = -1
		increment_j = 1
		temp_pos = (king[0]+increment_i, king[1]+increment_j)
		while self.inBounds(temp_pos):
			temp_sq = board[temp_pos[0]][temp_pos[1]]
			if temp_sq != self.blank_space:
				if temp_sq in enemy_piece:
					return True
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)
			

		increment_i = 1
		increment_j = -1
		temp_pos = (king[0]+increment_i, king[1]+increment_j)
		while self.inBounds(temp_pos):
			temp_sq = board[temp_pos[0]][temp_pos[1]]
			if temp_sq != self.blank_space:
				if temp_sq in enemy_piece:
					return True
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)
			

		increment_i = -1
		increment_j = -1
		temp_pos = (king[0]+increment_i, king[1]+increment_j)
		while self.inBounds(temp_pos):
			temp_sq = board[temp_pos[0]][temp_pos[1]]
			if temp_sq != self.blank_space:
				if temp_sq in enemy_piece:
					return True
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)
			


		# move like rook
		enemy_piece = (enemy_pieces[0], enemy_pieces[4])
		increment_i = 1
		increment_j = 0
		temp_pos = (king[0]+increment_i, king[1]+increment_j)
		while self.inBounds(temp_pos):
			if board[temp_pos[0]][temp_pos[1]] != self.blank_space:
				if board[temp_pos[0]][temp_pos[1]] in enemy_piece:
					return True
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)
			

		increment_i = 0
		increment_j = 1
		temp_pos = (king[0]+increment_i, king[1]+increment_j)
		while self.inBounds(temp_pos):
			if board[temp_pos[0]][temp_pos[1]] != self.blank_space:
				if board[temp_pos[0]][temp_pos[1]] in enemy_piece:
					return True
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)
			

		increment_i = -1
		increment_j = 0
		temp_pos = (king[0]+increment_i, king[1]+increment_j)
		while self.inBounds(temp_pos):
			if board[temp_pos[0]][temp_pos[1]] != self.blank_space:
				if board[temp_pos[0]][temp_pos[1]] in enemy_piece:
					return True
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)
			

		increment_i = 0
		increment_j = -1
		temp_pos = (king[0]+increment_i, king[1]+increment_j)
		while self.inBounds(temp_pos):
			if board[temp_pos[0]][temp_pos[1]] != self.blank_space:
				if board[temp_pos[0]][temp_pos[1]] in enemy_piece:
					return True
				break
			temp_pos = (temp_pos[0]+increment_i, temp_pos[1]+increment_j)
			

		return False

	def createsCheck(self, move, side):
		# check if moving side's piece checks its own king
		# including if king moves into a captureable position
		pass

	# def find_start_pos(piece_type, cols=[i for i in range(len(8))], rows=[i for i in range(len(8))]):
	# 	for file in cols:
	# 		for rank in rows:
	# 			if self.board[file][rank] == piece_type:
	# 				# change to object
	# 				piece.canCapture(self.board, side, end_pos)

	# (OPTIONAL) TODO Check if board is valid

	def decipher(self, move, side):
		# Function converts chess notation to the actual moving piece on the board
		# Raises exception if there is a piece blocking the move in-between the sqs (but does not check if piece on sq)
		# Raises exception if starting/captured piece can not be found
		# Raises exception for ambiguous moves on the board
		# Assumes en_passant square is correct, does no extra checking
		# col_index_convert = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
		# major_pieces = {"K", "Q", "N", "B", "R"}

		piece_class = None
		start_pos = -1 # stores board indexes such as (4,3) for e4
		end_pos = -1
		promoted_piece = self.blank_space # change to type of promoted_piece
		capture_flag = False
		double_pawn = None # changes to en passant square
		castle = self.blank_space

		# check for castle
		if move in ("0-0", "O-O"):
			castle = "0-0"
			return (piece_class, start_pos, end_pos, promoted_piece, capture_flag, double_pawn, castle)
		if move in ("0-0-0", "O-O-O"):
			castle = "0-0-0"
			return (piece_class, start_pos, end_pos, promoted_piece, capture_flag, double_pawn, castle)


		# check for capture
		capture_index = move.find('x')
		if capture_index != -1:
			capture_flag = True
			move = move[:capture_index] + move[capture_index+1:]

		# throw away moves without sufficient information
		if len(move) < 2:
			raise InvalidMove

		# TODO (OPTIONAL) SUPPORT CAPTURE FLAG WITHOUT 'X' IN NOTATION
		# For major piece move,
		if move[0].upper() in self.major_pieces:
			# get piece type
			major_piece_type = move[0]
			piece_class = major_piece_type

			# find start and end pos
			if side == Side.BLACK:
				major_piece_type = major_piece_type.lower()

			if len(move) == 3:
				end_pos = (self.col_index_convert[move[1]], int(move[2])-1)

				# get start pos
				piece = getObject[piece_class]()
				capturing_pieces = piece.canCapture(self.board, side, end_pos)
				if len(capturing_pieces) > 1:
					raise AmbiguousMove("Multiple {}s can move to {}".format(piece_class, end_pos))
				if len(capturing_pieces) == 0:
					raise InvalidMove("Cannot find the piece to move")
				start_pos = capturing_pieces[0]

			if len(move) == 4:
				end_pos = (self.col_index_convert[move[2]], int(move[3])-1)

				# get start pos
				piece = getObject[piece_class]()
				capturing_pieces = piece.canCapture(self.board, side, end_pos)
				if move[1].isalpha():
					file = self.col_index_convert[move[1]]
					for i in range(len(capturing_pieces)):
						if capturing_pieces[i][0] == file:
							if start_pos != -1:
								raise AmbiguousMove("Multiple {} in file {} can move to {}".format(piece_class, move[1], end_pos))
							else:
								start_pos = capturing_pieces[i]
				else:
					rank = int(move[1])
					for i in range(len(capturing_pieces)):
						if capturing_pieces[i][1] == rank-1:
							if start_pos != -1:
								raise AmbiguousMove("Multiple {} in row {} can move to {}".format(piece_class, move[1], end_pos))
							else:
								start_pos = capturing_pieces[i]
				if start_pos == -1:
					raise InvalidMove("Cannot find the piece to move")

			if len(move) == 5:
				end_pos = (self.col_index_convert[move[3]], int(move[4])-1)
				# get start pos
				piece = getObject[piece_class]()
				capturing_pieces = piece.canCapture(self.board, side, end_pos)
				start_pos = (self.col_index_convert[move[1]], int(move[2])-1)
				if self.board[start_pos[0]][start_pos[1]] != major_piece_type:
					raise InvalidMove("Cannot find {} at {}".format(major_piece_type, start_pos))

				

		# decipher Pawn move
		else:
			# check for capture
			if move[1].isalpha():
				capture_flag = True
				end_pos = (self.col_index_convert[move[1]], int(move[2])-1)
				backstep = -1 if side == Side.WHITE else 1
				start_pos = (self.col_index_convert[move[0]], int(move[2]) + backstep - 1)
				target = 'P' if side == Side.WHITE else 'p'
				if self.board[start_pos[0]][start_pos[1]] != target:
					raise InvalidMove("Cannot find the piece to move")

				# check for en passant flag
				enemy_target = 'p' if side == Side.WHITE else 'P'
				if end_pos != self.enpassant and self.board[end_pos[0]][end_pos[1]] != enemy_target:
					raise InvalidMove("Cannot find the piece to capture")

			else:
				end_pos = (self.col_index_convert[move[0]], int(move[1])-1)
				target = 'P' if side == Side.WHITE else 'p'
				backstep = -1 if side == Side.WHITE else 1
				if self.board[end_pos[0]][end_pos[1] + backstep] == target:
					start_pos = (end_pos[0], end_pos[1] + backstep)
				# check for double pawn move
				elif self.board[end_pos[0]][end_pos[1] + 2*backstep] == target:
					if self.board[end_pos[0]][end_pos[1] + backstep] != '-':
						raise InvalidMove("Pawn cannot move through piece on {}".format((end_pos[0], end_pos[1] + backstep)))
					start_pos = (end_pos[0], end_pos[1] + 2*backstep)
					double_pawn = (end_pos[0], end_pos[1] + backstep)
				else:
					raise InvalidMove("Cannot find the piece to move")
		
			# check for promotion
			if move[-1].upper() in self.major_pieces:
				promoted_piece = move[-1].upper()

			piece_class = 'P'

		 
		return (piece_class, start_pos, end_pos, promoted_piece, capture_flag, double_pawn, castle)

	def containsEnemy(self, sq, board, side):
		piece = board[sq[0]][sq[1]]
		if side == side.WHITE:
			return piece.islower()
		else:
			return piece.isupper()

	def legalMove(self, start_pos, end_pos, piece_type, side):
		# check if pawn is indeed capturing if moving diagonally or on starting pos if moving twice
		if piece_type.upper() == "P":
			if start_pos[0] != end_pos[0]:
				if not self.containsEnemy(end_pos, self.board, side) and end_pos not in self.enpassant:
					raise InvalidMove("{} pawn cannot capture {}".format(start_pos, self.board[end_pos[0]][end_pos[1]]))
			if abs(int(start_pos[1]) - int(end_pos[1])) > 1:
				if side == Side.WHITE and start_pos[1] != 1:
					raise InvalidMove("White Double Pawn Move is illegal on row {} (Chess row {})".format(start_pos[1], start_pos[1]+1))
				if side == Side.BLACK and start_pos[1] != 6:
					raise InvalidMove("Black Double Pawn Move is illegal on row {} (Chess row {})".format(start_pos[1], start_pos[1]+1))

		# check if move lands within board limits
		if not self.inBounds(end_pos):
			raise InvalidMove("Move to {} is out of bounds".format(end_pos))

		# check if ending sq is already occupied by a friendly piece
		end_pos_piece = self.board[end_pos[0]][end_pos[1]]
		if end_pos_piece != '-':
			if side == Side.WHITE and end_pos_piece.isupper():
				raise InvalidMove("End Square Occupied by {}".format(end_pos_piece))
			if side == Side.BLACK and end_pos_piece.islower():
				raise InvalidMove("End Square Occupied by {}".format(end_pos_piece))

		# check if moving would place king in check
		board_copy = [col[:] for col in self.board]
		board_copy[end_pos[0]][end_pos[1]] = board_copy[start_pos[0]][start_pos[1]]
		board_copy[start_pos[0]][start_pos[1]] = self.blank_space
		if self.inCheck(board_copy, side):
			raise InvalidMove("Moving from {} to {} puts King in check".format(start_pos, end_pos))

		return True

	def immmovableKing(self):
		# locate king position
		to_locate = ''
		enemy_pieces = ['Q','K','N','B','R','P']
		if side == Side.WHITE:
			to_locate = 'K'
			enemy_pieces = [x.lower() for x in enemy_pieces]
		if side == Side.BLACK:
			to_locate = 'k'

		king = ''
		# print("To locate: {}".format(to_locate))
		for i in range(len(board)):
			for j in range(len(board)):
				if board[i][j] == to_locate:
					king = (i,j)

		end_poses = [(king[0]+1, king[1]+1), (king[0]+1, king[1]), (king[0]+1, king[1]-1), (king[0], king[1]+1), (king[0], king[1]-1), (king[0]-1, king[1]+1), (king[0]-1, king[1]), (king[0]-1, king[1]-1)]
		for end_pos in end_poses:
			illegal = True
			try:
				self.legalMove(king, end_pos, 'K', self.turn)
				illegal = False
			except InvalidMove:
				pass
			if illegal == False:
				return False

		return True

	# Types of moves involve:
		# Piece Capture 
		# Move 
		# En Passant 
		# Promotion 
		# Castle 

	# TODO Allow Draw Offer and Accept
	# takes in Short algebraic notation
	# moving king or rook voids castling rights
	def move(self, move, side):
		move = move.strip()
		# = for draw or end game

		decoded_move = self.decipher(move, side) # TODO Put this in Try...Catch
		# decipher calls canCapture() so guarantees there are valid pieces in the move
		piece_type = decoded_move[0]
		start_pos = decoded_move[1] # stores board indexes such as (4,3) for e4
		end_pos = decoded_move[2]
		promoted_piece = decoded_move[3]
		capture_flag = decoded_move[4]
		double_pawn = decoded_move[5]
		castling = decoded_move[6]
		
		# check for castling rights, void if king or rook moves
		# assumes castling is in ('0-0', '0-0-0', self.blank_space)
		if castling != self.blank_space:
			permission = "Q"
			king = "K"
			king_cols = (2,5)
			inbetween_cols = (1,4)
			king_row = 0
			if castling == "0-0":
				permission = "K"
				king_cols = (4,7)
				inbetween_cols = (5,7)
			elif castling != "0-0-0":
				raise Exception("Castling flag raised, but move is not a valid castle")
			if side == Side.BLACK:
				king = king.lower()
				permission = permission.lower()
				king_row = 7

			# does king have castling rights?
			if permission not in self.castle_rights:
				raise InvalidMove("Side {} does not have rights to {}".format(side, castling))

			# Are pieces out of the way?
			for sq in [(col,king_row) for col in range(inbetween_cols[0], inbetween_cols[1])]:
				if self.board[sq[0]][sq[1]] != self.blank_space:
					raise InvalidMove("{} on {} in way of castle {}".format(self.board[sq[0]][sq[1]], sq, castling))

			# does move through check?
			board_copy = [col[:] for col in self.board]
			board_copy[4][king_row] = self.blank_space
			for sq in [(col,king_row) for col in range(king_cols[0], king_cols[1])]:
				board_copy[sq[0]][sq[1]] = king
				if self.inCheck(board_copy, side):
					raise InvalidMove("Castling moves king through check on {}".format(sq))
				else:
					board_copy[sq[0]][sq[1]] = self.blank_space

			# make move
			king_col = 2
			rook_start = 0
			rook_end = 3
			if castling == "0-0":
				king_col = 6
				rook_start = 7
				rook_end = 5

			# move king
			self.board[king_col][king_row] = self.board[4][king_row]
			self.board[4][king_row] = self.blank_space
			# move rook
			self.board[rook_end][king_row] = self.board[rook_start][king_row]
			self.board[rook_start][king_row] = self.blank_space

			# castle rights
			king_right = 'K'
			queen_right = 'Q'
			if side == Side.BLACK:
				king_right = king_right.lower()
				queen_right = queen_right.lower()
			self.castle_rights = self.castle_rights.replace(king_right, '').replace(queen_right, '')

		# check for legal move on board
		else:
			try:
				self.legalMove(start_pos, end_pos, piece_type, side)
			except (AmbiguousMove, InvalidMove):
				raise

			# make move and update previous space as self.blank_space
			if promoted_piece.upper() in self.major_pieces:
				piece = promoted_piece.upper() if side == Side.WHITE else promoted_piece.lower()
				self.board[end_pos[0]][end_pos[1]] = piece
			else:
				self.board[end_pos[0]][end_pos[1]] = self.board[start_pos[0]][start_pos[1]]
			self.board[start_pos[0]][start_pos[1]] = self.blank_space

			# castle rights
			to_remove = self.blank_space
			if piece_type.upper() == 'R':
				if start_pos == [0,0]:
					to_remove = 'Q'
				if start_pos == [7,0]:
					to_remove = 'K'
				if start_pos == [0,7]:
					to_remove = 'q'
				if start_pos == [7,7]:
					to_remove = 'k'
			if to_remove != self.blank_space:
				self.castle_rights = self.castle_rights.replace(to_remove, '')

			if piece_type.upper() == 'K':
				king_right = 'K'
				queen_right = 'Q'
				if side == Side.BLACK:
					king_right = king_right.lower()
					queen_right = queen_right.lower()
				self.castle_rights = self.castle_rights.replace(king_right, '').replace(queen_right, '')



		# get rid of old en passants and add new en passant if double move pawn
		self.enpassant = '-'
		if double_pawn is not None:
			self.enpassant = double_pawn

		# update halfmove clock
		if capture_flag or piece_type == 'P':
			self.half_moves = 0
		else:
			self.half_moves += 1
		
		# make sure to check for halfmove clock for Draws
		if self.half_moves >= 50:
			return Result.DRAW

		# update active color
		self.turn = Side.BLACK if side == Side.WHITE else Side.WHITE

		# check for repetition
		fen = self.exportFEN()
		curr = (fen.split()[0], fen.split()[1])
		repeat_count = 0
		for prev_fen in self.log:
			prev = (prev_fen.split()[0], prev_fen.split()[1])
			if prev == curr:
				repeat_count += 1
			if repeat_count >= 2:
				return Result.DRAW

		# record in log
		self.log.append(fen)

		# increment fullmoves
		self.full_moves += 1

		# if game is over, return a Result
		opp_side = Side.BLACK if side == Side.WHITE else Side.WHITE
		if self.inCheck(self.board, opp_side) and self.immmovableKing():
			return Result.WIN

		# returns 2 for valid move
		return 2
		

	def exportFEN(self):
		piece_placement = []
		for i in range(len(self.board[0])-1, -1, -1):
			
			j = 0
			empty_sq_count = 0
			while j < len(self.board):	
				if self.board[j][i] != self.blank_space:
					if empty_sq_count > 0:
						piece_placement.append(str(empty_sq_count))
					piece_placement.append(self.board[j][i])
				elif j == len(self.board)-1:
					empty_sq_count += 1
					piece_placement.append(str(empty_sq_count))
				else:
					empty_sq_count += 1
				j += 1
			if i != 0:
				piece_placement.append('/')

		piece_placement = "".join(piece_placement)

		active_color = str(self.turn)
		castling_rights = self.castle_rights
		en_passant_targets = self.enpassant
		if self.enpassant != '-':
			en_passant_targets = str(self.num_to_alpha[self.enpassant[0]]) + str(self.enpassant[1]+1)
		half_move_clock = str(self.half_moves)
		full_move_clock = str(self.full_moves)

		fen = [piece_placement, active_color, castling_rights, en_passant_targets, half_move_clock, full_move_clock]
		return " ".join(fen)


	def export(self, path):
		# TODO (OPTIONAL) RECORD MOVES DURING GAME IN PGN AND EXPORT
		print("Printing to {}".format(path))
		pass

	def printLog(self):
		pass

	def printBoard(self):
		print("{} to move:".format((self.turn).value.upper()))
		for i in range(len(self.board)-1, -1, -1):
			for j in range(len(self.board[0])):
				print(self.board[j][i], end=' ')
			print()

def printbyrc(game):
	cont_ = True
	while cont_:
		line = input("Give row/col\n")
		if line.lower() == "stop":
			cont_ = False
		if line[0] == 'c':
			col = int(line[1:])
			print(game.board[col])
		if line[0] == 'r':
			row = int(line[1:])
			print([col[row] for col in game.board])

		print()

def testDecipher(moves, FEN):
	game = Board(FEN)

	for move in moves:	
		try:
			print(game.decipher(move, game.turn))
		except Exception as e:
			print("Raise {}: {}".format(type(e), str(e)))

def testMove(moves, FEN):
	game = Board(FEN)
	print("Starting position ", end='')
	game.printBoard()
	print()

	for move in moves:
		game.move(move, game.turn)
		game.printBoard()
		print()
		game = Board(FEN)

if __name__ == "__main__":
	# Asks for move 
	# keeps track of side to move
	# can import and export boards
	# can end and begin games

	# moves = ["Qd3", "Qdd3", "Q2d6", "Qbd3", "Qd2d3", "Nh2", "Ng3", "N3h2"]
	# testDecipher(moves, "r4rk1/1qnbPppp/1b1p4/1p2p2n/1P1QP3/1Q2BN1P/R2Q1PP1/RN3NK1 w - - 0 1")

	# moves = ["Qd3", "Qdd3", "Q2d6", "Qbd3", "Qd2d3", "Nh2", "Ng3", "N3h2"]
	moves = ["0-0", "0-0-0", "Qe7"]
	testMove(moves, "r3k2r/pppq1ppp/2npbn2/2b1p3/2B1P3/2NPBN2/PPP1QPPP/R3K2R b KQkq - 7 8")

