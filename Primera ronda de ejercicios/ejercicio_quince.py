'''
Crear un programa que imprima por pantalla todo lo que el usuario ingresa 
hasta que ingresa la palabra “salir”
'''
i = 0
banco_palabras = []
palabra = ''

while palabra != 'salir':
	palabra = input("ingresa una palabra:  ")
	banco_palabras.append(palabra)

for i in range(len(banco_palabras)):
	print(banco_palabras[i])
