# Crear matriz 3x4 con todos los asientos libres (0)
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Pedir fila y columna al usuario
fila = int(input("Ingrese la fila (0-2): "))
columna = int(input("Ingrese la columna (0-3): "))

# Reservar el asiento
asientos[fila][columna] = 1

# Mostrar la matriz usando bucles anidados
print("\nEstado de la sala:")
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()

