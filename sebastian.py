def editar_empanada(empanadas):

    nombre = input("Ingrese el nombre de la empanada que desea editar: ").strip()

    for empanada in empanadas:
        if empanada["nombre"] == nombre:

            nuevo_nombre = input("Nuevo nombre: ").strip()

            while True:
                try:
                    nuevo_precio = float(input("Nuevo precio: "))
                    break
                except ValueError:
                    print("Error: debe ingresar un número válido")

            nuevos_ingredientes = input("Nuevos ingredientes: ").strip()

            while True:
                nueva_disponibilidad = input("Disponible (si/no): ").strip().lower()
                if nueva_disponibilidad in ["si", "no"]:
                    break
                else:
                    print("Error: solo puede escribir 'si' o 'no'")

            empanada["nombre"] = nuevo_nombre
            empanada["precio"] = nuevo_precio
            empanada["ingredientes"] = nuevos_ingredientes
            empanada["disponible"] = nueva_disponibilidad

            print("Empanada editada correctamente")
            return

    print("Empanada no encontrada")