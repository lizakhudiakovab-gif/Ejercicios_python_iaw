notas = []

for i in range(5):
    nota = float(input("Introduce una nota: "))
    notas.append(nota)

print("Notas:", notas)
print("Media:", sum(notas) / 5)
print("Mayor:", max(notas))
print("Menor:", min(notas))
