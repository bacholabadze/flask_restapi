from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from ..models.item_model import ItemModel


class Item(Resource):
    """Parser helps to get the only desired information to update an existing item
    required=True ==> no request can come through with no price."""
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='price field cannot be left blank!')
    parser.add_argument('store_id', type=int, required=True, help='store_id field cannot be left blank!')

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

        item = ItemModel(name, data['price'], data['store_id'])

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
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']
            item.store_id = data['store_id']
        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}
