import random

numero_secreto = random.randint(1, 100)

for num_intento in range(1, 11):
    numero = int(input("Introduce un número del 1 al 100: "))

    if numero == numero_secreto:
        print("Lo has acertado en",num_intento, "intentos")
        break

    elif numero < numero_secreto:
        print("El número secreto es mayor.")

    else:
        print("El número secreto es menor.")

    print("Te quedan", 10 - num_intento, "intentos.")

else:
    print("Has perdido. El numero secreto era:", numero_secreto)


