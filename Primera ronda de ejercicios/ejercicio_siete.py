print("Bienvenido al banco!\nPor favor ingrese el monto que va a invertir:  ")

while True:
  try:
    monto_invertido = float(input())
    dinero_post_inversion = monto_invertido * 5 / 100 * 6 + monto_invertido
    break
  except:
    print("Intente nuevamente con un número.")

print("Al cabo de 6 meses usted tendra " + str(dinero_post_inversion))
