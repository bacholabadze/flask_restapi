from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

items = []


class Item(Resource):

    """Parser helps to get the only desired information to update an existing item
    required=True ==> no request can come through with no price."""
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='This field cannot be left blank!')

    @jwt_required()
    def get(self, name):

        """next builtin function returns 'the first' item, founded by filter
        next can cause error if there is no item, if we don't pass default param None"""
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {"item": item}, 200 if item else 400

    def post(self, name):
        """parameters for get_json() :
         (force=True) =>> this will format content-type header to be application/Json (!!!Dangerous)
         (silent=True) =>> this will return None if data IS NOT Json format"""
        # Data now is parsed
        # data = request.get_json()

        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {f"message": f"An item with name {name} already exists."}, 400

        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {"message": 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {"name": name, 'price': data['price']}
            items.append(item)
        else:
            print(item)
            print(data)
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
app.run(port=5000, debug=True)
