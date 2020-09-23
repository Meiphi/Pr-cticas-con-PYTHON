import math

class Punto:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

	def __str__(self):
		print(f'({self.x}, {self.y})')

	def cuadrante(self):
		if self.x == 0 and self.y != 0:
			print('se sitúa sobre el eje Y')
		elif self.x != 0 and self.y == 0:
			print('se sitúa sobre el eje X')
		elif self.x == 0 and self.y == 0:
			print('está sobre el origen')

	def vector(self, p):
		vector = (p.x - self.x  ,  p.y - self.x)
			print(vector)

	def distancia(self, p):
		d = math.sqrt( pow(self.y - self.x, 2) + pow(p.y - p.x, 2) )
		print(f'la distancia es {d}')

A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3, -1)
D = Punto(0,0)

A.vector(B)
C.vector(D)

D.cuadrante()

# A(2, 3), B(5,5), C(-3, -1) y D(0,0)

		