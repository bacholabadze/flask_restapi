from flask_restful import Resource, reqparse
from ..models.user_model import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='user must have username.')
    parser.add_argument('password', type=str, required=True, help='user must have password.')

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"Error": "User already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()
        return {"message": "User created successfully."}, 201
