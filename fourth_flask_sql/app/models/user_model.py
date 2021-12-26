import sqlite3
from ..dataBase.db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))  # To limit characters to 80
    password = db.Column(db.String(80))


    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect("app/dataBase/data.db")
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
        connection = sqlite3.connect("app/dataBase/data.db")
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

