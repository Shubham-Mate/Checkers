class Player:
	def __init__(self, color, pieces):
		self.color = color
		self.pieces = pieces

	def getPieces(self):
		return self.pieces

	def removePiece(self, piece):
		self.pieces.remove(piece)