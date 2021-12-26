import sqlite3
from flask_restful import Resource, reqparse

from ..models.user_model import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='user must have username.')
    parser.add_argument('password', type=str, required=True, help='user must have password.')

    def post(self):
        data = UserRegister.parser.parse_args()

        # Check if user already exists
        if UserModel.find_by_username(data['username']):
            return {"Error": "User already exists"}, 400

        connection = sqlite3.connect("app/dataBase/data.db")
        cursor = connection.cursor()

        insert_query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(insert_query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201
