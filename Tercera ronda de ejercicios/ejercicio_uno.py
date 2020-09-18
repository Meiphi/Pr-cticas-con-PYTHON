'''
Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@".
'''
#funcion para validar un email
def validar_email(email):
	for arroba in email:
		if arroba == '@':
			return True
	return False

#funcion para pedir email y retorna el email ingresado
def pedir_email():
	print('Por favor ingrese su email:')
	email = input()
	return email

#### COMIENZA PROGRAMA

print('Programa para validar emails.')

email = pedir_email()

while True:
	if validar_email(email): #si el email es valido o no
		print("Válido")
		break
	else:
		print("No valido")
		email = ''
		email = pedir_email()
