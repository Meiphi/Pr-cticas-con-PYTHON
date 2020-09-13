'''
Crear un programa que recorra un diccionario previamente creado y muestre por pantalla:
'''

nick_usuario = "Mensa"
clave_usuario  = "Mensa123"
nombre_usuario = "Malena"
apellido_usuario = "Cadima"
estado_cuenta = 1

usuario = {
	"nick"		: nick_usuario,
	"clave"		: clave_usuario,
	"name"		: nombre_usuario,
	"surname"	: apellido_usuario,
	"status"	: estado_cuenta
}

for data, valor  in usuario.items():
	print(str(data) + '	---->	' + str(valor))

