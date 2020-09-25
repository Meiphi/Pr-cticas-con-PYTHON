'''
Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma)
'''

#funcion para pedir números y retorna una list con todos los numeros
def pedir_datos():
	numero = int(input())
	list_numeros = [numero]
	while numero != 0:
		numero = int(input())
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

print("Programa para sumar todos lo números que quiera!\nIngrese un cero para calcular la suma de los números ingresados.")

list_numeros = pedir_datos()
print(list_numeros)
resultado = sumatoria(list_numeros)
print(f'La suma de todos sus números: {resultado}')






