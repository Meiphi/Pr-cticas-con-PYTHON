'''
Se ingresa una edad, mostrar por pantalla alguna de las siguientes
leyendas:
‘menor’ si la edad es menor o igual a 12
‘cadete’ si la edad está comprendida entre 13 y 18
‘juvenil’ si la edad es mayor que 18 y no supera los 26
‘mayor’ en el caso que no cumpla ninguna de las condiciones anteriores.
'''

def determinar_estado(edad):
	if edad > 26:
		return 'mayor'
	elif 18 < edad and edad <= 26:
		return 'juvenil'
	elif 13 < edad and edad <= 18:
		return 'cadete'
	else:
		return 'menor'

print("Ingrese su edad para determinar un estado")
edad = int(input())
print(determinar_estado(edad))
