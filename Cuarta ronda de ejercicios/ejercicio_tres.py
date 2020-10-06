'''
Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
- Un constructor, donde los datos pueden estar vacios.
- Mostrar(): Muestra los datos de la persona.
- esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
'''

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

#---> Programa Principal

usuario = Persona('Delfi', 30, 40123123)
usuario.mostrar()
print('Es mayor de edad') if usuario.esMayorDeEdad() else print('Es menor de edad')

print('')

usuario_dos = Persona('Camila', 9, 725807)
usuario_dos.mostrar()
print('Es mayor de edad') if usuario_dos.esMayorDeEdad() else print('Es menor de edad')



