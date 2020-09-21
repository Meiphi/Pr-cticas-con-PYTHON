'''
11. Realizar una función llamada ​ area_rectangulo(base, altura)​ que devuelva el área del rectángulo a partir de una base y una altura. Calcular el área de un rectángulo de15 de base y 10 de altura.
'''
def area_rectangulo(base, altura):
	return base * altura / 2

print("Programa #11")
num_base = float(input("Ingrese la base del rectángulo:  "))
num_altura = float(input("Ingrese la altura del rectángulo:  "))
print("%.2f" % area_rectangulo(num_base, num_altura))
