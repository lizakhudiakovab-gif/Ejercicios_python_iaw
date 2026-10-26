nota1 = float(input("Introduce la primera nota parcial: "))
nota2 = float(input("Introduce la segunda nota parcial: "))
nota3 = float(input("Introduce la tercera nota parcial: "))

examen = float(input("Introduce la nota del examen final: "))
trabajo = float(input("Introduce la nota del trabajo final: "))

promedio = (nota1 + nota2 + nota3) / 3

nota_final = promedio * 0.55 + examen * 0.30 + trabajo * 0.15

print("La nota final es:", nota_final)
