import json
from flask import Flask, request, jsonify

FILE_NAME  = 'tasks.json'

app = Flask(__name__)

VALID_STATUSES = ["To Do", "In Progress", "Completed"]


def read_tasks():
    with open(FILE_NAME, 'r', encoding= "utf-8") as f:
        return json.load(f)


def write_tasks(tasks):
    with open (FILE_NAME, 'w', encoding="utf-8") as f:
        json.dump(tasks, f, indent= 2)


@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = read_tasks()
    status = request.args.get('status')

    if status:
        tasks = [t for t in tasks if t['status'] == status]

    return jsonify(tasks), 200


@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body must be valid JSON"}), 400

    tasks = read_tasks()

    if not data.get('id'):
        return jsonify({"error": "Missing id"}), 400

    if any(t['id'] == data['id'] for t in tasks):
        return jsonify({"error": "A task with this id already exists"}), 400

    if not data.get('title'):
        return jsonify({"error": "Missing title"}), 400

    if not data.get('description'):
        return jsonify({"error": "Missing description"}), 400

    if not data.get('status'):
        return jsonify({"error": "Missing status"}), 400

    if data['status'] not in VALID_STATUSES:
        return jsonify({"error": f"Invalid status. Must be one of {VALID_STATUSES}"}), 400

    new_task = {
        "id": data['id'],
        "title": data['title'],
        "description": data['description'],
        "status": data['status']
    }
    tasks.append(new_task)
    write_tasks(tasks)

    return jsonify(new_task), 201


@app.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Request body must be valid JSON"}), 400

    tasks = read_tasks()

    task = next((t for t in tasks if t['id'] == id), None)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    if 'status' in data and data['status'] not in VALID_STATUSES:
        return jsonify({"error": f"Invalid status. Must be one of {VALID_STATUSES}"}), 400

    task['title'] = data.get('title', task['title'])
    task['description'] = data.get('description', task['description'])
    task['status'] = data.get('status', task['status'])

    write_tasks(tasks)
    return jsonify(task), 200


@app.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    tasks = read_tasks()
    task = next((t for t in tasks if t['id'] == id), None)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    tasks.remove(task)
    write_tasks(tasks)

    return jsonify({"message": "Task deleted"}), 200



if __name__ == '__main__':
    app.run(debug=True)