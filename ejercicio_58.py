
nombres = []
edades = []

nombre = input("Nombre: ")

while nombre != "*":
    edad = int(input("Edad: "))
    nombres.append(nombre)
    edades.append(edad)
    nombre = input("Nombre: ")

if len(edades) > 0:
    mayor = max(edades)

    for i in range(len(nombres)):
        if edades[i] >= 18:
            print("Mayor de edad:", nombres[i])

        if edades[i] == mayor:
            print("Alumno más mayor:", nombres[i])
