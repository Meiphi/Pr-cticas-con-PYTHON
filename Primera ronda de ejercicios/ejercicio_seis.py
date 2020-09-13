print("Números positivos y sumas!\n Ingrese tantos números positivos como desee, para terminar aprete 0")

sumatoria = 0
aux = "0"

while aux != 0:
  sumatoria = sumatoria + int(aux)
  
  # VALIDANDO #
  while True:
    try:
      aux = int(input())
      if aux > 0: #es positivo
        print( "el numero es: " + str(aux) )
        break
      elif aux == 0: #finish
        break
      elif aux < 0: #es negativo
        print("ERROR DETECTADO: Ingrese un número positivo.")
        aux = 0
    except ValueError: #cuando ingresan otra cosa que no sea número type int
      print("ERROR DETECTADO: Ingrese un número positivo.")

print("Suma total de los núúmeros ingresados:  " + str(sumatoria))
