'''
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligado y la cantidad es opcional. Construye los siguientes métodos para la clase:
- Un constructor, donde los datos pueden estar vacios.
- El atributo no se puede modificar directamente, solo ingresando o retirando dinero
- mostrar(): Muestra los datos de la cuenta
- ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
- retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
'''

#clase persona para para clase titular
class Persona:
	def __init__(self, nombre = None, edad = None, dni = None):
		self.nombre = nombre
		self.edad = edad
		self.dni = dni
	
	def mostrar(self):
		print('Nombre: ', self.nombre)
		print('Edad: ', self.edad)
		print('DNI: ', self.dni)

	def esMayorDeEdad(self):
		if self.edad >= 18:
			return True
		else:
			return False

class Cuenta:
	def __init__(self, titular = None, cantidad = None):
		self.titular = titular
		self.cantidad = cantidad

	def mostrar(self):
		print('Titular:  ', self.titular)
		print('Cantidad: ', self.cantidad)

	def ingresar(self):
		cantidad_ingresada = float(input('Cantidad a ingresar: '))
		if cantidad_ingresada > 0:
			self.cantidad = self.cantidad + cantidad_ingresada
			print(f'Se ingreso {cantidad_ingresada}.-')
			print(f'Nuevo monto: {self.cantidad}.-')
		else:
			print('Acá no pasó nada xd')

	def retirar(self):
		cantidad_retirada = float(input(f'Cantidad a retirar: '))
		self.cantidad = self.cantidad - cantidad_retirada
		print(f'se reitró plata: {cantidad_retirada}')
		if self.cantidad < 0:
			print(f'números rojos xdxdxd: {self.cantidad}')
		else:
			print(f'Nuevo monto: {self.cantidad}')

usuario = Persona('Delfi', 30, 40123123)

usuario_cuenta = Cuenta( usuario.nombre, 10000 )

usuario_cuenta.mostrar()

usuario_cuenta.ingresar()

usuario_cuenta.retirar()
