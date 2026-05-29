from flask import Flask, request, jsonify

app = Flask(__name__)

data = ["Apple", "Banana"]

# GET
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

# POST
@app.route('/items', methods=['POST'])
def add_item():
    item = request.json['item']
    data.append(item)
    return jsonify({"message": "Item added"})

# PUT (Update)
@app.route('/items/<int:index>', methods=['PUT'])
def update_item(index):
    data[index] = request.json['item']
    return jsonify({"message": "Item updated"})

# DELETE
@app.route('/items/<int:index>', methods=['DELETE'])
def delete_item(index):
    data.pop(index)
    return jsonify({"message": "Item deleted"})

app.run(debug=True)