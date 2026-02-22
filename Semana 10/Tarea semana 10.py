# Programa con matriz de 3x3
# Objetivo: Declarar, recorrer e imprimir una matriz

# Declarar matriz de 3x3 con números enteros
matriz = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]

# Recorrer la matriz con ciclos anidados
print("Valores de la matriz:")
print()

for i in range(3):
    for j in range(3):
        print(f"matriz[{i}][{j}] = {matriz[i][j]}")

print()
print("Matriz en formato tabular:")
print()

for i in range(3):
    for j in range(3):
        print(f"{matriz[i][j]}", end=" ")
    print()