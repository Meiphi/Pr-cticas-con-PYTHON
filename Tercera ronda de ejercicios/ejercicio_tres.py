'''
Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. Reutilizar la misma función realizada en el ejercicio 2
'''

#funciones del ejercicio 2:

#funcion para pedir números y retorna una list con todos los numeros
def pedir_datos():
	numero = int(input())
	list_numeros = [numero]
	suma_digitos(numero)
	while numero != 0:
		numero = int(input())
		#aca llamar a una funcion que sume los digitos del número
		suma_digitos(numero)
		list_numeros.append(numero)
	return list_numeros

def suma_digitos(num):
	digitos_del_numero = []
	while num // 10 != 0:
		resto = num % 10
		digitos_del_numero.append(resto)
		num = num // 10
	digitos_del_numero.append(num)
	res_suma_digitos = 0
	for i in digitos_del_numero:
		res_suma_digitos = i + res_suma_digitos
	print("suma de sus digitos: ", res_suma_digitos)



#funcion sumatoria, recibe una lista de números y retorna la suma de todos
def sumatoria(list_numeros):
	res_sumatoria = 0
	i = 0
	for i in list_numeros:
		res_sumatoria =  res_sumatoria + i 
	return res_sumatoria


### COMIENZA PROGRAMA
print("Programa para sumar todos lo números que quiera!\nIngrese un cero para calcular la suma de los números ingresados.\nTambién suma digitos")

list_numeros = pedir_datos()



sumatoria = sumatoria(list_numeros)

print(f'total: {sumatoria}')

suma_digitos(sumatoria)










