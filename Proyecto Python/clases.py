class Detector:
    def __init__(self, matriz):
        self.matriz = matriz
        self.filas = len(matriz)
        self.columnas = len(matriz[0])

    def detectar_mutantes(self):
        return self.detectar_horizontal() or self.detectar_vertical() or self.detectar_diagonal()

    def detectar_horizontal(self):
        for fila in self.matriz:
            for i in range(self.columnas - 3):
                if fila[i] == fila[i+1] == fila[i+2] == fila[i+3]:
                    return True
        return False

    def detectar_vertical(self):
        for col in range(self.columnas):
            for row in range(self.filas - 3):
                if self.matriz[row][col] == self.matriz[row+1][col] == self.matriz[row+2][col] == self.matriz[row+3][col]:
                    return True
        return False

    def detectar_diagonal(self):
        for row in range(self.filas - 3):
            for col in range(self.columnas - 3):
                if self.matriz[row][col] == self.matriz[row+1][col+1] == self.matriz[row+2][col+2] == self.matriz[row+3][col+3]:
                    return True
                if self.matriz[row][col+3] == self.matriz[row+1][col+2] == self.matriz[row+2][col+1] == self.matriz[row+3][col]:
                    return True
        return False

class Mutador:
    def __init__(self, base_nitrogenada):
        self.base_nitrogenada = base_nitrogenada

    def crear_mutante(self):
        pass

class Radiacion(Mutador):
    def __init__(self, base_nitrogenada):
        super().__init__(base_nitrogenada)

    def crear_mutante(self, matriz, posicion_inicial, orientacion_de_la_mutacion):
        try:
            if orientacion_de_la_mutacion == "H":
                for i in range(4):
                    matriz[posicion_inicial[0]] = matriz[posicion_inicial[0]][:posicion_inicial[1] + i] + self.base_nitrogenada + matriz[posicion_inicial[0]][posicion_inicial[1] + i + 1:]
            elif orientacion_de_la_mutacion == "V":
                for i in range(4):
                    matriz[posicion_inicial[0] + i] = matriz[posicion_inicial[0] + i][:posicion_inicial[1]] + self.base_nitrogenada + matriz[posicion_inicial[0] + i][posicion_inicial[1] + 1:]
            else:
                raise ValueError("Orientación no válida")
            return matriz
        except IndexError:
            print("Posición inicial fuera de los límites de la matriz")
        except Exception as e:
            print(f"Error: {e}")

class Virus(Mutador):
    def __init__(self, base_nitrogenada):
        super().__init__(base_nitrogenada)

    def crear_mutante(self, matriz, posicion_inicial):
        try:
            for i in range(4):
                matriz[posicion_inicial[0] + i] = matriz[posicion_inicial[0] + i][:posicion_inicial[1] + i] + self.base_nitrogenada + matriz[posicion_inicial[0] + i][posicion_inicial[1] + i + 1:]
            return matriz
        except IndexError:
            print("Posición inicial fuera de los límites de la matriz")
        except Exception as e:
            print(f"Error: {e}")

class Sanador:
    def __init__(self):
        self.bases = ["A", "T", "C", "G"]

    def sanar_mutantes(self, matriz):
        detector = Detector(matriz)
        if detector.detectar_mutantes():
            return self.generar_nuevo_adn()
        return matriz

    def generar_nuevo_adn(self):
        import random
        return ["".join(random.choices(self.bases, k=6)) for _ in range(6)]