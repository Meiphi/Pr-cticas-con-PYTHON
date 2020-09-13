"""
Dada un número entero de la forma (AAAAMMDD), que representa una
fecha válida mostrar el día, mes y año que representa.
"""

fecha = int(input("ingrese una fecha formato AAAAMMDD:  "))

#20200910

año = int(fecha / 10000)
	#2020

mes = int(fecha / 100) - int(año * 100) 
	#202009 - #202000

dia = fecha -  año * 10000 - mes * 100  
	#20200910 - 20200000 - 0900

print("día: " + str(dia))

print("mes: " + str(mes))

print("año: " + str(año))
