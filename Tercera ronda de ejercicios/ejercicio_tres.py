'''
Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. Reutilizar la misma función realizada en el ejercicio 2
'''

#funciones del ejercicio 2:

#funcion para pedir números y retorna una list con todos los numeros
def pedir_datos():
	numero = int(input())
	list_numeros = [numero]
	while numero != 0:
		numero = int(input())
		#aca tiene que llamar a una funcion que sume los digitos del número
		list_numeros.append(numero)
	return list_numeros


#funcion sumatoria, recibe una lista de números y retorna la suma de todos
def sumatoria(list_numeros):
	res_sumatoria = 0
	i = 0
	for i in list_numeros:
		res_sumatoria =  res_sumatoria + i 
	return res_sumatoria


### COMIENZA PROGRAMA
print("Programa para sumar todos lo números que quiera!\nIngrese un cero para calcular la suma de los números ingresados. También suma digitos")

list_numeros = pedir_datos()



sumatoria(list_numeros)











