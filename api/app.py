from flask import Flask, request, jsonify

app = Flask(__name__)

tareas = []

@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    return jsonify(tareas)

@app.route('/tareas', methods=['POST'])
def agregar_tarea():
    data = request.get_json()
    tarea = {
        'id': len(tareas) + 1,
        'titulo': data.get('titulo'),
        'completado': False
    }
    tareas.append(tarea)
    return jsonify(tarea), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
