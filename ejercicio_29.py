base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

resultado = 1

for i in range(exponente):
    resultado = resultado * base

print("Resultado:", resultado)
