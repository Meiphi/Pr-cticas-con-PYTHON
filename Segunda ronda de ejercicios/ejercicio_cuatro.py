'''
Dados dos valores enteros y distintos, emitir una leyenda apropiada que
informe cuál es el mayor entre ellos
'''

print('En este programa analizaremos dos números e informaremos el mayor de ellos')

valor_uno = int(input("Primer valor:  "))

valor_dos = int(input("Segundo valor:  "))

if valor_uno > valor_dos:
	print('El número ', valor_uno, ' es mayor a ', valor_dos, ".")
else:
	print('El número ', valor_dos, ' es mayor a ', valor_uno, ".")