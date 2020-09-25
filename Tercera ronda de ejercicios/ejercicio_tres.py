''' Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. Reutilizar la misma función realizada en el ejercicio 2 '''
#funciones del ejercicio 2:

#funcion para pedir números y retorna una list con todos los numeros
def pedir_datos():
	numero = None
	list_numeros = []
	while numero != 0:
		numero = int(input('Ingrese un número:  '))
		#aca llamar a una funcion que sume los digitos del número
		print('Suma de digitos: ',suma_digitos(numero), '\n')
		list_numeros.append(numero)
	return list_numeros

def suma_digitos(num):
	digitos_del_numero = []

	while num // 10 != 0:
		digitos_del_numero.append(num % 10) #me quedo con los restos 
		num = num // 10
 
	digitos_del_numero.append(num) # tengo los números separados pero en orden inverso jajaja
	return sum(digitos_del_numero) #por prop comutativa de la suma, da igual que esten inversos

#funcion sumatoria, recibe una lista de números y retorna la suma de todos
def sumatoria(list_numeros):
	return sum(list_numeros)


### COMIENZA PROGRAMA
print('Programa #3')
list_numeros = pedir_datos()

sumatoria = sumatoria(list_numeros)
print(f'total: {sumatoria}')
print('Suma de digitos de la suma total: ', suma_digitos(sumatoria))