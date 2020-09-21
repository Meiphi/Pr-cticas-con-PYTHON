'''
16. Crear una función que, a partir de un mensaje, nos devuelva una lista con todos los números, si los hay, que aparecen en dicho mensaje.
'''

def detector_numeros(mensaje):
	list_numeros = []
	for i in mensaje.split():
		if i.isdigit():
			list_numeros.append(i)
	return list_numeros

print('Programa #16')
print(detector_numeros(input('Mensaje:  ')))
