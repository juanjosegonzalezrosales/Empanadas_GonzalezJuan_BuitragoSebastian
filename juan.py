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