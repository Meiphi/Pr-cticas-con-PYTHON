'''
12. Realizar una función llamada ​ intermedio(a, b)​ que a partir de dos números, devuelva su punto intermedio.
'''

def intermedio(a, b):
	return (b - a)/2

print("Programa #12")
print("%.2f" % intermedio(float(input("Ingrese el primer punto de partida:  ")), float(input("Ingrese el segundo punto de partida:  "))))
