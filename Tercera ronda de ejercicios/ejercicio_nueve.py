'''
9. Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios al principio o al final del string pasado por parámetro.
'''

def ultima_palabra(frase):
	posicion_ult_palabra = len(frase.split()) - 1
	return frase.split()[posicion_ult_palabra]

print("Comienza programa")
frase = input("Ingrese una frase:  ")
palabra = ultima_palabra(frase)
print(palabra)
