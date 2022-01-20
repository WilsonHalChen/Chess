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

	@staticmethod
	@abstractmethod
	def canCapture(board, side, target):
		# returns piece pos' of opposite side that can capture target
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

	def canCapture(board, side, target):
		enemy_pieces = ['Q','K','N','B','R','P']
		if side == Side.WHITE:
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

	def canCapture(board, side, target):
		enemy_pieces = ['Q','K','N','B','R','P']
		if side == Side.WHITE:
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

	def canCapture(board, side, target):
		enemy_pieces = ['Q','K','N','B','R','P']
		if side == Side.WHITE:
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

	def canCapture(board, side, target):
		enemy_pieces = ['Q','K','N','B','R','P']
		if side == Side.WHITE:
			enemy_pieces = [x.lower() for x in enemy_pieces]
		result = []
		enemy_piece = enemy_pieces[2]
		knight_moves = [(target[0]+1, target[1]+2), (target[0]+1, target[1]-2), (target[0]-1, target[1]+2), (target[0]-1, target[1]+2),
						(target[0]+2, target[1]+1), (target[0]+2, target[1]-1), (target[0]-2, target[1]+1), (target[0]-2, target[1]+1)]
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

	def canCapture(board, side, target):
		enemy_pieces = ['Q','K','N','B','R','P']
		if side == Side.WHITE:
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

	def canCapture(board, side, target):
		enemy_pieces = ['Q','K','N','B','R','P']
		if side == Side.WHITE:
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

	def inCheck(self, board, side):
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

	def decipher(self, move, side):
		# move is guaranteed not to be castle
		# side indicates who is to move
		# col_index_convert = ['a','b','c','d','e','f','g','h']
		# major_pieces = {"K", "Q", "N", "B", "R"}

		piece_type = -1
		start_pos = -1 # stores board indexes such as (4,3) for e4
		end_pos = -1
		promoted_piece = -1
		capture_flag = False
		double_pawn = False
		en_passant = -1

		# For major piece move,
		if move[0] in self.major_pieces:
			major_piece_type = move[0]
			if side == Side.BLACK:
				major_piece_type = major_piece_type.lower()

			if len(move) == 3:
				end_pos = (col_index_convert.find(move[1]), int(move[2]))
			if len(move) == 4:
				end_pos = (col_index_convert.find(move[2]), int(move[3]))
				if not move[1].isnumeric():
					file = col_index_convert.find(move[1])
					for rank in range(len(self.board[0])):
						if self.board[file][rank] == major_piece_type:
							start_pos = (file, rank)
							break
				else:
					rank = int(move[1])
					for file in range(len(self.board)):
						if self.board[file][rank] == major_piece_type:
							start_pos = (file, rank)
							break
			if len(move) == 5:
				end_pos = (col_index_convert.find(move[3]), int(move[4]))
				start_pos = (col_index_convert.find(move[1]), int(move[2]))
				
		# Get piece type
		# find end pos, check if it is a capture

		# Check for Pawn move
		# set capture if contains 'x'

		# For pawn move, set piece type 
		# find end pos, and which pawn can move to it
		# check for en passant flag
		# check for promotion
		# check for double pawn move

		 
		return (piece_type, start_pos, end_pos, promoted_piece, capture_flag, double_pawn, en_passant)

	def legalMove(self, start_pos, end_pos, piece_type):
		# check if piece can legally move toward that position

		# check if pawn is indeed capturing if moving diagonally or on starting pos if moving twice

		# check if moving would place king in check

		# check if move lands in empty square within board limits

		# check if move is blocked by a piece
		pass

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
		# check for repetition

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
	# game = Board("4q3/r3b2n/3p1kp1/1p1bpp2/1Pp3P1/2P1BN2/2BN1P2/Q5K1 w - - 0 38")
	# game.printBoard()
	# print(game.inCheck(game.board, Side.BLACK))

	game = Board("4q3/r3b2n/3p1kp1/1p1bpp2/1Pp3P1/2P1BN2/2BN1P2/Q5K1 w - - 0 38")
	game.printBoard()
	board = game.board