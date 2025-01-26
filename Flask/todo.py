from flask import Flask,request,jsonify

app = Flask(__name__)

items = [
    {"id": 1, "name": "Item One", "description": "This is the first item."},
    {"id": 2, "name": "Item Two", "description": "This is the second item."},
    {"id": 3, "name": "Item Three", "description": "This is the third item."}
]

@app.route('/')
def home():
    return "Welcome to the To Do List!!!"

@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"]==item_id))
    if item is None:
        return jsonify({"Error" : "Item not found"})
    else:
        return jsonify(item)
    

@app.route('/items',methods=['POST'])
def create_items():
    if not request.json or not 'name' in request.json:
        return jsonify({"Error" : "Item not found"})
    else:
        new_item={
            'id': items[-1]["id"]+1 if items else 1,
            'name':request.json['name'],
            'description':request.json['description']
        }
        items.append(new_item)
        return jsonify(new_item)
    
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"]==item_id))
    if item is None:
        return jsonify({"Error" : "Item not found"})
    else:
        item['name'] = request.json.get('name',item['name'])
        item['description'] = request.json.get('description',item['description'])
    return jsonify(item)

@app.route('/items/<int:item_id>',methods=['DELETE'])
def del_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'Result':'Item deleted'})

    


if __name__ == "__main__":
    app.run(debug=True)