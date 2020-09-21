'''
15. Crear una función que devuelva una lista con todos los números pares del 0 al 100 inclusive. Imprimir esa lista por pantalla.
'''

def list_pares():
	num_pares = []
	for i in range(101):
		if i % 2 == 0:
			num_pares.append(i)
	return num_pares

print('Programa #15')
print(list_pares())