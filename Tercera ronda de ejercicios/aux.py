'''EJERCICIO #20 
- Crear un diccionario con 10 estudiantes y sus respectivas notas. 

- Luego crear una función que nos informe los estudiantes aprobados (nota >= 7), los estudiantes desaprobados (4 <= nota < 7) y los estudiantes aplazados (0 <= nota < 4).'''


dic_alumnos = {
	'alumno_0' :	0,
	'alumno_0_4' :	2,
	'alumno_4' :	4,
	'alumno_4_7':	5,
	'alumno_7' :	7,
	'alumno_7_10' :	8,
	'alumno_10' :	10
}

lis_aprobados = [] 
lis_desaprobados = []
lis_aplazados = []


for alumno,nota in dic_alumnos.items():
	if nota >= 7:
		lis_aprobados.append(alumno)
		

print(lis_aprobados.join(x))

