'''EJERCICIO #20 
- Crear un diccionario con 10 estudiantes y sus respectivas notas. 

- Luego crear una función que nos informe los estudiantes aprobados (nota >= 7), los estudiantes desaprobados (4 <= nota < 7) y los estudiantes aplazados (0 <= nota < 4).'''


#Función obtener diccionario
#Parametros: Ninguno
#Retorna: Un diccionario de alumnos y sus notas
def obtener_diccionario():
	alumnos ={
		'alumno_0' :	0,
		'alumno_0_4' :	2,
		'alumno_4' :	4,
		'alumno_4_7':	5,
		'alumno_7' :	7,
		'alumno_7_10' :	8,
		'alumno_10' :	10
	}
	return alumnos
#fin obtener_diccionario()


#Función analisis de notas 
#Parametros: El diccionario con los alumnos y sus notas
#Retorna: retorne una tupla con tres listas de alumnos
def analisis_de_notas(dic_alumnos):
	#si tenemos un diccionario, lista, o tupla tenemos que tener en mente "Es muy probable que tenga que recorrerlo con un for"
	# for   LLAVE   in   DICCIONARIO:
	#bloque de código
	lis_aprobados = [] 
	lis_desaprobados = []
	lis_aplazados = []

	for alumno,nota in dic_alumnos.items():
		if nota >= 7:
			lis_aprobados.append(alumno)
			#print('alumno aprobado: ',alumno)
		elif nota >= 4 and nota <7:
			lis_desaprobados.append(alumno)
			#print('alumno desaprobado: ', alumno)
		elif nota < 4:
			lis_aplazados.append(alumno)
			#print('alumno aplazado: ', alumno)
	return lis_aprobados, lis_desaprobados, lis_aplazados






#----> PROGRAMA PRINCIPAL <----

dic_alumnos_notas = obtener_diccionario() #nos devuelve algo? SÍ; Entonces tengo que guardarlo en una variable!!

#--pausa: que tenemos hasta acá? un diccionario de alumnos y notas cargado. Y ahora que hago? Informo el estado de los alumnos.
tup_estado_alumno = analisis_de_notas(dic_alumnos_notas)

#--pausa: Vamos a hacer las funciones.

print('Alumnos aprobados: ', tup_estado_alumno[0])
print('Alumnos desaprobados: ', tup_estado_alumno[1])
print('Alumnos aplazados: ', tup_estado_alumno[2])














