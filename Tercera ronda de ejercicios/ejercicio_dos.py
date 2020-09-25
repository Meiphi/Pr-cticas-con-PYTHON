'''
Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma)
'''

#funcion para pedir números y retorna una list con todos los numeros
def pedir_datos():
	numero = None
	list_numeros = []
	while numero != 0:
		numero = int(input('Ingrese un número: '))
		#llama a la suma_digitos
		print('Suma de digitos: ', suma_digitos(numero), '\n')
		list_numeros.append(numero)
	return list_numeros


#funcion sumatoria, recibe una lista de números y retorna la suma de todos
def suma_digitos(num):
	digitos_del_numero = []
	
	while num // 10 != 0:
		resto = num % 10
		digitos_del_numero.append(resto)
		num = num // 10

	digitos_del_numero.append(num)
	
	return sum(digitos_del_numero)

### COMIENZA PROGRAMA

print("Programa #2")

list_numeros = pedir_datos()






