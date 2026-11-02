a = int(input("Límite inferior: "))
b = int(input("Límite superior: "))

while a >= b:
    a = int(input("Límite inferior: "))
    b = int(input("Límite superior: "))

suma = 0
contador = 0
igual = False

while True:
    n = int(input("Número: "))

    if n == 0:
        break

    if a < n < b:
        suma += n
        contador += 1

    if n == a or n == b:
        igual = True

print("Suma:", suma)
print("Cantidad:", contador)
print("Igual a algún límite:", igual)
