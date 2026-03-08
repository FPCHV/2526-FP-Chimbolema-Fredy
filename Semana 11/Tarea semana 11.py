# Crear una matriz de tamaño 5x5
matriz = []

print("=== Ingreso de datos para la Matriz 5x5 ===\n")

# Pedir valores al usuario e ingresar en la matriz
for fila in range(5):
    fila_datos = []
    for columna in range(5):
        # Solicitar el valor al usuario
        while True:
            try:
                valor = float(input(f"Ingrese valor para posición [{fila}][{columna}]: "))
                fila_datos.append(valor)
                break
            except ValueError:
                print("Error: Ingrese un número válido")
    matriz.append(fila_datos)

# Mostrar la matriz ingresada en forma de tabla
print("\n=== Matriz ingresada ===\n")
for fila in range(5):
    for columna in range(5):
        print(f"{matriz[fila][columna]:8.2f}", end=" ")
    print()  # Saltar de línea

print("\n¡Matriz completada exitosamente!")