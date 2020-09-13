print("Resolvemos: (3*8/2)² ")

num = 3 * 8 / 2 

# num = int(input("número: "))

i = 0

res = num

for i in range(2):
	res = num * res

print("Respuesta:  " + str(res))