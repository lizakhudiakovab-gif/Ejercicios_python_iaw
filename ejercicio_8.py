sueldo = float(input("Introduce el sueldo base: "))
venta1 = float(input("Introduce la primera venta: "))
venta2 = float(input("Introduce la segunda venta: "))
venta3 = float(input("Introduce la tercera venta: "))

comisiones = (venta1 + venta2 + venta3) * 0.10
total = sueldo + comisiones

print("Comisiones:", comisiones)
print("Sueldo total:", total)

