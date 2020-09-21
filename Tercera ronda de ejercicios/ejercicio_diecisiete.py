'''
17. Crear una función que devuelva True si los parámetros ingresados son todos números, False si hay al menos uno de los parámetros ingresados que no es un número, y None si ninguno de los parámetros ingresados es un número. Imprimir resultado por pantalla.
'''

def son_numeros(*args):
	no_verificados = 0
	for arg in args:
		if not isinstance(arg, int):
			no_verificados = no_verificados + 1
	if no_verificados == len(args):
		return None
	elif no_verificados >= 1:
		return False
	return True

print("Programa #17")
print("Si son todos números:\t\t\t", son_numeros(1,2,3,4,5))
print("Si son numeros y letras:\t\t", son_numeros(1,'b',3,4))
print('Si ningun parámetro es un número:\t', son_numeros('a'))