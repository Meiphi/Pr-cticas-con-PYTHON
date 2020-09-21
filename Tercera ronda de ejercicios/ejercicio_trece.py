'''13. Realizar una función ​ separar(lista)​ que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares y la segunda con los números impares.
'''
def separar(lista_num):
	num_pares = []
	num_impares = []
	for num in lista_num:
		if num % 2 == 0:
			num_pares.append(num)
		else:
			num_impares.append(num)
	list_pares = num_pares.sort()
	list_impares = num_impares.sort()
	return num_pares, num_impares #retorna una tupla

print("Programa #13")
list_num = [10,3,4,7,1,2]
listas = separar(list_num)
print(listas)