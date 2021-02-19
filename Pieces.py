import pygame

class Piece:
	def __init__(self, color, isKing, UID, isSelected):
		self.color = color
		self.isKing = isKing
		self.radius = 30
		self.UID = UID
		self.isSelected = isSelected

	def setKing(self):
		self.isKing = True

	def setSelected(self, setBool):
		self.isSelected = setBool

	def drawSelf(self, window, center):
		pygame.draw.circle(window, self.color, center, self.radius)
		self.center = center

	def getCenter(self):
		return self.center

	def getSelected(self):
		return self.isSelected

	