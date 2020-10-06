#PROGRAMA QUE LEE UNA PALABRA Y LA CIFRA CON CLAVE 3

mensaje = 'HOLA'

# print('ubicacion en la tabla ascii de la letra "a":  ',ord('a'))

# print('letra en la tabla ascii de la posicion 97:  ',chr(97))

#print(ord('A'))

clave = 3

print(mensaje)

#print(chr(ord('A') + 3))

# recorrer el string
for key in mensaje:
	print( chr( ord(key) + 3 ), end = '')

print('')



