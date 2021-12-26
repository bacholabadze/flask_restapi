import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from ..models.item_model import ItemModel


class Item(Resource):
    """Parser helps to get the only desired information to update an existing item
    required=True ==> no request can come through with no price."""
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='This field cannot be left blank!')

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": f"An item with name '{name}' already exists"}

        data = Item.parser.parse_args()

        item = ItemModel(name, data['price'])

        try:
            item.save_to_db()
        except:
            return {"Error": "Item inserting failed"}, 500
        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"message": "Item deleted"}
        return {"message": "Item could not be found"}

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, data['price'])
        else:
            item.price = data['price']
        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect("app/dataBase/data.db")
        cursor = connection.cursor()

        query = 'SELECT * FROM items'
        result = cursor.execute(query)
        items = []
        for row in result:
            print(row)
            items.append({'name': row[0], 'price': row[1]})
        print(items)
        connection.close()
        return {'items': items}
