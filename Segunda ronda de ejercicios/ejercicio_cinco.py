'''
Dadas dos fechas informar cual es la más reciente. Determine cuales
serían los datos de entrada y las leyendas a informar de acuerdo al
proceso solicitado.
'''

#funcion de mensaje de error
def error():
	print("ERROR: Esa fecha no existe. Ingrese de nuevo la fecha.")

#funcion para validar las fechas, devuelve falso si la fecha no existe
def validar_fecha(dia, mes):
	if mes < 1 or mes > 12: #fuera de Enero a Diciembre
		error()
		return(False)
	elif dia < 1 or dia > 31: #fuera del dia 1 al 31
		error()
		return(False)
	elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia == 31: #meses que terminan en 30
		error()
		return(False)
	elif mes == 2 and dia > 28: #febrero es especial, no tuve en cuenta los años biciestos
		error()
		return(False)
	else:
		return(True)

#funcion para pedir fechas y retorna una tupla fecha con el dia mes y año
def pedir_fecha():
	dia = int(input("dia: "))
	mes = int(input("mes: "))
	año = int(input("año: "))

	while not validar_fecha(dia, mes):
		pedir_fecha()

	fecha = dia, mes, año

	return fecha


#funcion que compara las dos fecha y determina la más reciente al dia de la fecha
def evaluar_fecha_reciente(t_primera_fecha, t_segunda_fecha) #recibi dos tuplas
	if t_primera_fecha[2] > t_segunda_fecha[2]: #si año1 es mayor a año2
		



#*******COMIENZA PROGRAMA

print("Programa para determinar la fecha más reciente.")

#Pido las fechas y las valido

##PRIMERA FECHA
print('Primera fecha')
t_primera_fecha = pedir_fecha() #guarda una tupla con la fecha = dia, mes, año

##SEGUNDA FECHA
print('Segunda fecha')
t_segunda_fecha = pedir_fecha() #guarda una tupla con la fecha = dia, mes, año

evaluar_fecha_reciente(t_primera_fecha, t_segunda_fecha) #envio dos tuplas















