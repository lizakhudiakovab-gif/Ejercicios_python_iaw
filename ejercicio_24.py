positivos = 0
negativos = 0
ceros = 0

cantidad = int(input("¿Cuántos números vas a introducir? "))

for i in range(cantidad):
    numero = int(input("Introduce un número: "))

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1

print("Positivos:", positivos)
print("Negativos:", negativos)
print("Ceros:", ceros)


