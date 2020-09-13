'''
Crear un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
'''

palabra = input("Ingrese una palabra:  ")
i = 0
for i in range(10):
	print(str(i + 1) + ". " + palabra)
