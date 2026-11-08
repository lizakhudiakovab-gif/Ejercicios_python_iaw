meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

numero = int(input("Introduce un mes del 1 al 12: "))

print("Mes:", meses[numero - 1])
print("Días:", dias[numero - 1])
