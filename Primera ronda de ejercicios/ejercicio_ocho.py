while True:
	try:
		edad = int(input("Ingrese su edad:  "))
		if edad < 120:	
			if edad >= 18:
				print("Usted es mayor de edad. Ya puede ir a la carcel")
				break
			else:
				print("Usted aun no es mayor de edad. Pero podrían llevarlo a una correpcional para menores.")
				break
		else:
			print("Ingrese su número de edad real")
	except ValueError:
		print("Ingrese su edad en números")