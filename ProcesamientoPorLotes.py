procesos = int(input("Ingresa el Numero de Procesos: "))
ID = int(input("Ingresa el ID: "))
NombreProgramador = input("Ingresa el Nombre del Programador: ")
TME = int(input("Ingresa el Tiempo Maximo Estimado: "))
Operacion = input("Ingresa la Operacion: ")
Num1 = int(input("Ingresa el Primer Numero: "))
Num2 = int(input("Ingresa el Segundo Nuemero: "))
#TR = input("Ingresa el Tiempo Transcurrido: ")

ContadorGlobal = 1
#int procesos2
#int procesos3

if ContadorGlobal > 5:
	Loteuno = 1
	print("Segundo Lote")
	print(Loteuno)
	ContadorGlobal += 1
	procesos -= 1
	print("Procesos Restantes: " + procesos)


if procesos < 5:
	Lotedos = 1
	print("El proceso es menor a 5")
	print(Lotedos)
