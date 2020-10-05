print('Programa #9')
# Crear un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla 
# si la contraseña introducida por el usuario coincide con la guardada 
# en la variable sin tener en cuenta mayúsculas y minúsculas.

clave = "Contraseña"
clave_ingresada = input("Ingrese la clave:  ")

if clave.lower() == clave_ingresada.lower():
  print('CORRECTO')
else:
  print('INCORRECTO')