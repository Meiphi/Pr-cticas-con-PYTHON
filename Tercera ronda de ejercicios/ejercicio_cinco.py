'''
5. Escribir un programa que pida números al usuario, mostrar el factorial de cada uno y, al finalizar, la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.
'''

#funcion pedir numeros
def pedir_datos(list_numeros):	
	print("Ingrese un \"0\" para finalizar.")
	num = None
	while num != 0:
		num = int(input("Ingrese número:  "))
		list_numeros.append(num)
		#llamar a la funcion factorial;
		calc_factorial(num)
	return list_numeros


#funcion factorial de cada número
def calc_factorial(num):
	factorial = 1
	for i in range(num):
		factorial = factorial * (i + 1)
	print(factorial)



#funcion sumatoria de los numeros solicitados
def sumatoria(list_numeros):
	res_sumatoria = 0
	i = 0
	for i in list_numeros:
		res_sumatoria =  res_sumatoria + i 
	return res_sumatoria


#COMIENZA PROGRAMA

print("Este programa te informa el factorial de los números que ingreses y la suma de todos.")

list_numeros = []
list_numeros = pedir_datos(list_numeros)
res_sumatoria = sumatoria(list_numeros)
print("Suma total de números ingresados:  ", res_sumatoria)




