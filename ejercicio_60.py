
tabla = []

for i in range(5):
    fila = []

    for j in range(5):
        numero = int(input("Introduce un número: "))
        fila.append(numero)

    tabla.append(fila)

for fila in tabla:
    print("Suma de fila:", sum(fila))

for j in range(5):
    suma = 0

    for i in range(5):
        suma = suma + tabla[i][j]

    print("Suma de columna:", suma)
