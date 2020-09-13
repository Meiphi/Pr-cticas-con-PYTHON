'''
10. Crear un programa que pida al usuario dos números y 
muestre por pantalla el cociente de la división entre ellos 
siempre que el segundo número sea distinto de 0.
'''

print("Programa exclusivamente para dividir")

dividendo = int(input("Dividendo:  ")) 

divisor = int(input("Divisor:  "))

if divisor == 0:
	print("No se puede divir por cero.")
	divisor = int(input("Divisor:  "))

res = dividendo / divisor

print(str(dividendo) + " | " + str(divisor) + " = " + str(res) )
