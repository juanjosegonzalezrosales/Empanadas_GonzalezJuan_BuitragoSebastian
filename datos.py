import json

ARCHIVO = "empanadas.json"

def cargar_empanadas():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_empanadas(empanadas):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(empanadas, f, indent=4)