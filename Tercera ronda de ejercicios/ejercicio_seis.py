'''
6.	Escribir un programa que pida números positivos al usuario. 

	Mostrar el número cuya sumatoria de dígitos fue mayor y la cantidad de números cuya sumatoria de dígitos fue menor que 10. 

	Utilizar una o más funciones, según sea necesario.
'''

#funcion para pedir numeros positivos; 
#Retorna nuna lista de numeros;
def pedir_datos():	
	print("Ingrese un número positivo")
	num = None
	list_numeros = []
	while num != 0:
		num = int(input())
		if num > 0: 
			list_numeros.append(num)
			print("Ingrese otro o \"0\" para finalizar")
		elif num < 0:
			print("ERROR: No se admiten números negativos")
			pedir_datos() #vuelvo a pedir el numero
		else:
			break
	return list_numeros


#funcion para sumar digitos; Retorna el resultado de la suma de los digitos del numero ingresado por parametro
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
	return res_suma_digitos


#funcion para determinar el mayor; 
#Recibe por parametro una lista de numeros
#Retorna la posición en la lista del mayor numero
def mayor_num(list_suma_digitos):
	mayor = 0
	#posicion = 
	for i in list_suma_digitos: 
		if i > mayor:
			mayor = i
	

#funcion para determinar cant_num_con_sumaDigitos_menor_diez;


#----------> | COMIENZA PROGRAMA |

print("PROGRAMA 6:\nIngrese un \"0\" para finalizar.\n")

list_numeros = []
list_numeros = pedir_datos()

list_suma_digitos = [] #para armar una lista con la suma de digitos de cada numero de la lista de números ingresados

for i in list_numeros:
	num = suma_digitos(i)
	list_suma_digitos.append(num)

#una vez que se llena la lista de la suma de digitos, llamo a la funcion que determina cual es el mayor

mayor_num(list_suma_digitos)















