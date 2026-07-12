# v69422
# updated
from flask import Flask, jsonify, request

app = Flask(__name__)
todos = []

@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    todos.append({"id": len(todos)+1, "text": data["text"], "done": False})
    return jsonify(todos[-1]), 201

@app.route("/todos/<int:tid>", methods=["DELETE"])
def delete_todo(tid):
    global todos
    todos = [t for t in todos if t["id"] != tid]
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
