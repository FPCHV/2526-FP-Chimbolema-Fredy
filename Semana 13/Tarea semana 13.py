# Método que calcula el total de una compra
def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total


def main():
    # Valores de ejemplo
    precio = 10
    cantidad = 3

    # Llamar al método
    resultado = calcular_total(precio, cantidad)

    # Mostrar el resultado
    print("El total de la compra es:", resultado)


# Ejecutar el programa
if __name__ == "__main__":
    main()

