suma = 0
contador = 0

while True:
    numero = int(input("Hola,introduce un numero: "))

    if numero == 0:
        break

    suma = suma + numero
    contador = contador + 1

print("Suma:", suma)

if contador > 0:
    print("Media:", suma / contador)


