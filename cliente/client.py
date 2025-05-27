import requests
import time

time.sleep(5)  # Espera que la API arranque

# Agregar una nueva tarea
nueva_tarea = {"titulo": "Aprender Docker y Flask"}
res = requests.post('http://api:5000/tareas', json=nueva_tarea)
print("Tarea creada:", res.json())

# Obtener todas las tareas
res = requests.get('http://api:5000/tareas')
print("Lista de tareas:")
for tarea in res.json():
    print("-", tarea['titulo'], "| Completado:", tarea['completado'])
