from flask import Flask, request, jsonify
import mongoengine as me
from models.model import Item, Weapon, Armor, Potion, TradeGood

app = Flask(__name__)
me.connect(host="<HostString>", alias='default')

@app.route('/item', methods=['POST'])
def create_item():
    data = request.json
    try:
        item = Item(**data).save()
        return item.to_json(), 201
    except me.ValidationError as e:
        return str(e), 400

@app.route('/item/<item_id>', methods=['GET'])
def get_item(item_id):
    item = Item.objects(item_id=item_id).first()
    if item:
        return item.to_json()
    else:
        return jsonify({"error": "Item not found"}), 404
        

if __name__ == '__main__':
    app.run(debug=True)
