from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity

from app.resources.user import UserRegister
from app.resources.item import Item, ItemList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app/dataBase/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

# Endpoints
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from app.dataBase.db import db
    db.init_app(app)
    app.run(port=5000, debug=True)