"""
A partir de un valor entero ingresado por teclado, se pide informar:
a) La quinta parte de dicho valor
b) El resto de la división por 5
c) La séptima parte del resultado del punto a)
"""
print("Hola, este programa calculará tres casos. Seleccione el que necesite: ")


valor = float(input("Ingrese un valor:  "))

quinta_parte = valor / 5

resto = valor % 5

septima_parte = quinta_parte / 7

#Con la siguiente linea puedo mostrar el resultado con dos lugares después de la coma.

print('La quita parte es: {0:.2f}'.format(quinta_parte)) 
print('El resto de la división por 5 es: resto')
print('La septima parte de {0:.2f}'.format(quinta_parte) + ' es: {0:.2f}'.format(septima_parte))


