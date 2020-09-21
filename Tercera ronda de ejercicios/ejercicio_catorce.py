'''14. Crear una función que, a partir de un dato de entrada que sea en horas, nos informe cuántos minutos y cuántos segundos serían esas horas. Imprimir por pantalla dichos valores.
'''

def convertir(horas):
	minutos = horas * 60
	segundos = minutos * 60
	return minutos, segundos

print("Programa #14")
(minutos, segundos) = convertir(int(input("Ingrese cant de horas:  ")))
print("minutos = ", minutos, " y segundos = ", segundos)