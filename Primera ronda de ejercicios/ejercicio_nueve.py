'''

Crear un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla 
si la contraseña introducida por el usuario coincide con la guardada 
en la variable sin tener en cuenta mayúsculas y minúsculas.

'''

clave = "Contraseña"
i = 0
clave_ingresada = input("Ingrese la clave:  ")

print(chr(78)) #SALE N
print(ord('A')) #SALE 65


if len(clave) == len(clave_ingresada):
	for i in range(len(clave)):
		if ord(clave[i]) == ord(clave_ingresada[i]):
			print("letra ok: " + str(i))

		elif ord(clave[i]) > :
