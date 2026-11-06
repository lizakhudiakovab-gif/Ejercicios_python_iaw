cadena = input("Introduce una cadena: ")
subcadena = input("Introduce una subcadena: ")

if cadena[:len(subcadena)] == subcadena:
    print("Sí")
else:
    print("No")
