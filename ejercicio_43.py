cadena = input("Introduce una cadena: ")
letra = input("Introduce una letra: ")

while len(letra) != 1:
    letra = input("Introduce solo una letra: ")

print(cadena.count(letra))
