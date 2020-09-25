'''
4. Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito en el número, utilizando para ello una función que calcule la
frecuencia.
'''

#funcion que calcula la frecuencia de un dígito en un número:

def calc_frecuencia_digito(datos):
	#Cuántas veces se repite un digito en un número
	#Por ejemplo, en 1101 el digito 1 se repite 3 veces.
	contador_digitos = None
	for i in dato[0]:  
		if dato[1] == i:
			contador_digitos = contador_digitos + 1
	return contador_digitos

#funcion que pide datos al usuario:
def pedir_dato():
	#Pedir un número y un digito.
	num = input('Ingrese un número: ')
	digito = input('Ingrese un digito: ')
	datos = [num, digito]
	return datos

#COMIENZA EL PROGRAMA

print("Programa para calcular la frecuencia del dígito en un número")

#guarda una lista
datos = pedir_dato()


contador_digitos = calc_frecuencia_digito(datos)

print(f"En el número {datos[0]}, el digito {datos[1]} se repite: {contador_digitos} veces.")



