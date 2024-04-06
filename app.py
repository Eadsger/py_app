from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de itens (simulando um banco de dados)
itens = [
    {"id": 1, "nome": "Item 1"},
    {"id": 2, "nome": "Item 2"},
    {"id": 3, "nome": "Item 3"}
]

# Rotas para CRUD básico
@app.route('/itens', methods=['GET'])
def get_itens():
    return jsonify(itens)

@app.route('/itens/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in itens if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({'message': 'Item não encontrado'}), 404

@app.route('/itens', methods=['POST'])
def add_item():
    data = request.get_json()
    novo_item = {'id': len(itens) + 1, 'nome': data['nome']}
    itens.append(novo_item)
    return jsonify(novo_item), 201

@app.route('/itens/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in itens if item['id'] == item_id), None)
    if item:
        data = request.get_json()
        item.update(data)
        return jsonify(item)
    return jsonify({'message': 'Item não encontrado'}), 404

@app.route('/itens/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global itens
    itens = [item for item in itens if item['id'] != item_id]
    return jsonify({'message': 'Item excluído'})

if __name__ == '__main__':
    app.run(debug=True)
