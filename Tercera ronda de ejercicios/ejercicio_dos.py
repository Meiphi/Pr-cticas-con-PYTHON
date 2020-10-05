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


#funcion sumatoria, recibe un número y retorna la suma de sus digitos
def suma_digitos(num):
	digitos_del_numero = [] #cree una lista vacia para los digitos;
							# ej.: 133 => [1,3,3]	
	while num // 10 != 0:  #wea matematica
		resto = num % 10   #más wea matemática
		digitos_del_numero.append(resto)  # se va guardando desde el último dígito
		num = num // 10	
		
	digitos_del_numero.append(num) # o sea termina así [3,1,1]
	
	return sum(digitos_del_numero) #retorna la suma de 3+1+1 que es lo mismo que 1+1+3

### COMIENZA PROGRAMA

print("Programa #2")

list_numeros = pedir_datos()






