print("Programa para saber cuántas letras tiene su palabra\n")
palabra = input("Ingrese su nombre:  ")
i = 0
c = 0
for i in range(len(palabra)):
  c = c + 1

print("Numero de letras:  " + str(c))