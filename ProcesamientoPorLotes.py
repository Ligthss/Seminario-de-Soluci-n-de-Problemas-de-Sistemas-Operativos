
lotes = []  # Lista para almacenar los lotes de procesos

procesos = int(input("Ingresa el Numero de Procesos: "))
while True: 	
    if procesos > 0:
        if procesos > 5:
            print(f'El proceso actual de este segundo lote es el numero: {len(lotes) + 1}')
            lote = []  # Crear una lista para almacenar los procesos del lote

            for contadorid in range(procesos):
                print(f'Tu ID es: {contadorid}')
                NombreProgramador = input("Ingresa el Nombre del Programador: ")
                TME = int(input("Ingresa el Tiempo Maximo Estimado: "))
                Operacion = input("Ingresa la Operacion: ")
                Num1 = int(input("Ingresa el Primer Numero: "))
                Num2 = int(input("Ingresa el Segundo Numero: "))
                
                lote.append({
                    'ID': contadorid,
                    'NombreProgramador': NombreProgramador,
                    'TME': TME,
                    'Operacion': Operacion,
                    'Num1': Num1,
                    'Num2': Num2
                })

            lotes.append(lote)  # Agregar el lote a la lista de lotes

            print("Segundo Lote")
            ProcesosTerminados = lotes
			ProcesosFaltantes = 0
			print(procesos - ProcesosTerminados)
			#No 


        else:
            print("No se realizarán procesos menores o iguales a 0, intenta nuevamente")
            # Regresar al ciclo para ingresar otro valor de procesos
    else:
        break  # Salir del bucle si se ingresa un valor de procesos igual o menor a 0

# Imprimir la información de los lotes
for i, lote in enumerate(lotes):
    print(f"Lote {i + 1}:")
    for proceso in lote:
        print(f'Proceso ID: {proceso["ID"]}, Programador: {proceso["NombreProgramador"]}, TME: {proceso["TME"]}, Operación: {proceso["Operacion"]}, Num1: {proceso["Num1"]}, Num2: {proceso["Num2"]}')
