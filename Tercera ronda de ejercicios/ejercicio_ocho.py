'''
8. Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
'''

#funcion validar
def validar_dni(dni):
	if len(dni) == 7 or len(dni) == 8:
		return True
	else:
		return False


#----->PROGRAMA PRINCIPAL

print("---- Programa ----")

if validar_dni(input("Ingrese un dni: ")):
	print("DNI validado")
else:
	print("Esa cosa no es un DNI xd")
