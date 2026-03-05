def listar_empanadas(empanadas):

    if len(empanadas) == 0:
        print("No hay empanadas registradas")
        return

    print("\n--- LISTA DE EMPANADAS ---")

    for empanada in empanadas:
        print("Nombre:", empanada["nombre"])
        print("Precio:", empanada["precio"])
        print("Ingredientes:", empanada["ingredientes"])
        print("Disponible:", empanada["disponible"])
        print("---------------------------")

def agregar_empanada(empanadas):

    print("\n--- AGREGAR EMPANADA ---")

    nombre = input("Nombre: ").strip()
    if nombre == "":
        print("Error: el nombre no puede estar vacío")
        return

    precio = input("Precio: ").strip()
    if precio == "":
        print("Error: el precio no puede estar vacío")
        return

    ingredientes = input("Ingredientes: ").strip()
    if ingredientes == "":
        print("Error: los ingredientes no pueden estar vacíos")
        return

    disponible = input("Disponible (si/no): ").strip()
    if disponible == "":
        print("Error: debe indicar si está disponible")
        return

    nueva_empanada = {
        "nombre": nombre,
        "precio": float(precio),
        "ingredientes": ingredientes,
        "disponible": disponible
    }

    empanadas.append(nueva_empanada)

    print("Empanada agregada correctamente")