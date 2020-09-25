'''
9. Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios al principio o al final del string pasado por parámetro.
'''

def long_ultima_palabra(frase):
	return len(frase.split()[-1])

print("Programa #9")
print(long_ultima_palabra(input("Ingrese una frase:  ")))
