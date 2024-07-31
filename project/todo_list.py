import json
import os


# Ruta del archivo JSON donde se guardarán las tareas
FILE_PATH = 'tareas.json'
tareas = {}
# Función para cargar las tareas desde el archivo JSON
def cargar_tareas():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as archivo:
            return json.load(archivo)
    return {}

# Función para guardar las tareas en el archivo JSON
def guardar_tareas(tareas):
    with open(FILE_PATH, 'w') as archivo:
        json.dump(tareas, archivo, indent=4)

# Función para agregar una tarea
def agregar_tarea(tareas):
    tarea = input("Ingrese la tarea a agregar: ")
    if tarea in tareas:
        print("La tarea ya existe en la lista.")
    else:
        tareas[tarea] = False
        print("Tarea agregada.")
        guardar_tareas(tareas)


def listar_tareas(tareas):
    if not tareas:
        print("\nNo hay tareas en la lista.")
    else:
        print("\nTiene las siguientes tareas")
        for tarea, completada in tareas.items():
            estado = "Completada" if completada else "Pendiente"
            print(f"{tarea}: {estado}")


def marcar_completada(tareas):
    tarea = input("Ingrese la tarea que desea marcar como completada: ")
    if tarea in tareas:
        tareas[tarea] = True
        print("Tarea marcada como completada.")
        guardar_tareas(tareas)
    else:
        print("La tarea no se encuentra en la lista.")


def limpiar_tareas(tareas):
    tareas.clear()
    print("Lista de tareas limpia.")
    guardar_tareas(tareas)

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Limpiar lista")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_tarea(tareas)
        elif opcion == '2':
            listar_tareas(tareas)
        elif opcion == '3':
            marcar_completada(tareas)
        elif opcion == '4':
            limpiar_tareas(tareas)
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    tareas = cargar_tareas()
    menu()
