
# Dedinimos la funcion con parametros y retorno
def calcular_promedio(nota1, nota2, nota3) :
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

# Entrada de datos
n1 = float(input("Ingrese la nota 1"))
n2 = float(input("Ingrese la nota 2"))
n3 = float(input("Ingrese la nota 3"))

#llamada a la funcion
resultado = calcular_promedio(n1, n2, n3)

# Mostrar el resultado
print("El promedio es:", resultado)
