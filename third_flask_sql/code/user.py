import sqlite3
from flask_restful import Resource, reqparse


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        ''' "WHERE" Filters to be only those rows where the username matches a parameter'''
        select_query = 'SELECT * FROM users WHERE username=?'

        ''' ! The Parameters have to be, even though it's single one, in the form of a tuple ! '''
        result = cursor.execute(select_query, (username,))

        ''' Gets the first row out of the result set. Returns None if there is not any'''
        row = result.fetchone()

        if row:
            # user = User(row[0], row[1], row[2])
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        ''' "WHERE" Filters to be only those rows where the username matches a parameter'''
        select_query = 'SELECT * FROM users WHERE id=?'

        ''' ! The Parameters have to be, even though it's single one, in the form of a tuple ! '''
        result = cursor.execute(select_query, (_id,))

        ''' Gets the first row out of the result set. Returns None if there is not any'''
        row = result.fetchone()

        if row:
            # user = User(row[0], row[1], row[2])
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='user must have username.')
    parser.add_argument('password', type=str, required=True, help='user must have password.')

    def post(self):
        data = UserRegister.parser.parse_args()

        # Check if user already exists
        if User.find_by_username(data['username']):
            return {"Error": "User already exists"}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        insert_query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(insert_query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201
