from datos import cargar_empanadas,guardar_empanadas
from sebastian import editar_empanada, eliminar_empanada
from juan import listar_empanadas,agregar_empanada
print("simulacion error")
def menu():

    empanadas = cargar_empanadas()

    while True:

        print("\n===== MENÚ EMPANADAS DOÑA PEPA =====")
        print("1. Listar empanadas")
        print("2. Agregar empanada")
        print("3. Editar empanada")
        print("4. Eliminar empanada")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_empanadas(empanadas)

        elif opcion == "2":
            agregar_empanada(empanadas)
            guardar_empanadas(empanadas)

        elif opcion == "3":
            editar_empanada(empanadas)
            guardar_empanadas(empanadas)

        elif opcion == "4":
            eliminar_empanada(empanadas)
            guardar_empanadas(empanadas)

        elif opcion == "5":
            guardar_empanadas(empanadas)
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()