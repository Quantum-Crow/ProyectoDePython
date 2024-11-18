from clases import Detector, Radiacion, Virus, Sanador

def main():
    matriz = []
    print("Ingrese la secuencia de ADN (6 filas de 6 caracteres cada una):")
    for _ in range(6):
        while True:
            fila = input()
            if len(fila) == 6 and all(c in "ATCG" for c in fila):
                matriz.append(fila)
                break
            else:
                print("Cada fila debe tener exactamente 6 caracteres y solo contener A, T, C, G. Intente de nuevo.")

    while True:
        print("\n¿Qué desea hacer?")
        print("1. Detectar mutaciones")
        print("2. Mutar el ADN")
        print("3. Sanar el ADN")
        print("4. Salir")
        opcion = input("Seleccione una opción (1, 2, 3 o 4): ")

        if opcion == "1":
            detector = Detector(matriz)
            if detector.detectar_mutantes():
                print("Se detectaron mutaciones en el ADN.")
            else:
                print("No se detectaron mutaciones en el ADN.")

        elif opcion == "2":
            print("¿Qué tipo de mutación desea crear?")
            print("1. Radiación (horizontal o vertical)")
            print("2. Virus (diagonal)")
            while True:
                tipo_mutacion = input("Seleccione una opción (1 o 2): ")
                if tipo_mutacion in ["1", "2"]:
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")

            if tipo_mutacion == "1":
                while True:
                    base_nitrogenada = input("Ingrese la base nitrogenada a repetir (A, T, C, G): ")
                    if base_nitrogenada in "ATCG":
                        break
                    else:
                        print("Base nitrogenada no válida. Intente de nuevo.")
                while True:
                    posicion_inicial = input("Ingrese la posición inicial (fila columna): ")
                    try:
                        posicion_inicial = tuple(map(int, posicion_inicial.split()))
                        if 0 <= posicion_inicial[0] < 6 and 0 <= posicion_inicial[1] < 6:
                            break
                        else:
                            print("Posición inicial fuera de los límites de la matriz. Intente de nuevo.")
                    except ValueError:
                        print("Formato de posición no válido. Intente de nuevo.")
                while True:
                    orientacion = input("Ingrese la orientación de la mutación (H para horizontal, V para vertical): ")
                    if orientacion in "HV":
                        break
                    else:
                        print("Orientación no válida. Intente de nuevo.")
                radiacion = Radiacion(base_nitrogenada)
                matriz = radiacion.crear_mutante(matriz, posicion_inicial, orientacion)

            elif tipo_mutacion == "2":
                while True:
                    base_nitrogenada = input("Ingrese la base nitrogenada a repetir (A, T, C, G): ")
                    if base_nitrogenada in "ATCG":
                        break
                    else:
                        print("Base nitrogenada no válida. Intente de nuevo.")
                while True:
                    posicion_inicial = input("Ingrese la posición inicial (fila columna): ")
                    try:
                        posicion_inicial = tuple(map(int, posicion_inicial.split()))
                        if 0 <= posicion_inicial[0] < 6 and 0 <= posicion_inicial[1] < 6:
                            break
                        else:
                            print("Posición inicial fuera de los límites de la matriz. Intente de nuevo.")
                    except ValueError:
                        print("Formato de posición no válido. Intente de nuevo.")
                virus = Virus(base_nitrogenada)
                matriz = virus.crear_mutante(matriz, posicion_inicial)

        elif opcion == "3":
            sanador = Sanador()
            matriz = sanador.sanar_mutantes(matriz)

        elif opcion == "4":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
            continue

        print("\nEste es el ADN actual:")
        for fila in matriz:
            print(fila)

if __name__ == "__main__":
    main()