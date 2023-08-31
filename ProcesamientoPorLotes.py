procesos = int(input("Ingresa el Numero de Procesos: "))
ID = int(input("Ingresa el ID: "))
NombreProgramador = input("Ingresa el Nombre del Programador: ")
TME = int(input("Ingresa el Tiempo Maximo Estimado: "))
Operacion = input("Ingresa la Operacion: ")
Num1 = int(input("Ingresa el Primer Numero: "))
Num2 = int(input("Ingresa el Segundo Numero: "))
#ResultadOperación, variable sin definir uso correcto aun, se corregirá después

ContadorTiempo = 1
#Este contador global servirá para el tiempo, en especifico un contador que lleve el tiempo desde el inicio hasta el final del programa.
#int procesos3

#El programa contara con N procesos, que seran conformados por lotes de 5 procesos cada 1
#El numero de procesos debe ser mayor a 0
#Para las operaciones se validará que no se hagan entre cero, y en caso de que realice operaciones entre cero, arrojar mensajes de error
#El programa imprimirá en pantalla los procesos en ejecución, los procesos terminados, y los procesos que faltan, así como
#los respectivos datos para cada proceso
#Se tomará el primer proceso que se ejecute como un proceso en ejecución
#En el lote trabajando se tendrán los datos del ID () y del tiempo maximo estimado (TME)
#En el proceso en ejecución se tendran los datos siguientes: Nombre del Programador, ID, Operación, 2 Numeros enteros para la operación, TME, Tiempo Transcurrido (TT)
#y Tiempo Restante (TR)
#Se mostrará en la sección principal de la pantalla el Numero de Lotes pendientes

if procesos > 5:
	procesos2 = 1
	print("Segundo Lote")
	print("Procesos Restantes: " + procesos - 1)


if procesos < 5:
	procesos3 = 1
	print("El proceso es menor a 5")
	print(procesos3)

#Las anteriores son validaciónes de prueba para verificar que las variables se declararon correctamente, y que las operaciones en variables
#cumplen su correcto funcionamiento
