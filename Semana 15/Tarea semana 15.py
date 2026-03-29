# 1. Creación de la colección (Diccionario)
agenda = {
    "Emergencias": "911",
    "Soporte": "01800"
}


def ejecutar_agenda():
    print("--- BIENVENIDO A TU GESTOR DE CONTACTOS ---")

    # 2. Agregar datos
    nombre = input("Ingresa el nombre del nuevo contacto: ")
    telefono = input(f"Ingresa el teléfono de {nombre}: ")
    agenda[nombre] = telefono
    print(f"\n✅ {nombre} ha sido guardado con éxito.")

    # 3. Mostrar la información almacenada (Recorrer elementos)
    print("\n--- LISTA DE CONTACTOS ACTUALIZADA ---")
    for nombre, tel in agenda.items():
        print(f"👤 Nombre: {nombre} | 📞 Tel: {tel}")

    # 4. Operación básica: Buscar un elemento
    print("\n--- BÚSQUEDA ---")
    busqueda = input("¿A quién deseas buscar?: ")

    if busqueda in agenda:
        print(f"🔎 Resultado: El número de {busqueda} es {agenda[busqueda]}")
    else:
        print(f"❌ El nombre '{busqueda}' no se encuentra en la agenda.")


# Ejecutar el programa
ejecutar_agenda()