import sqlite3


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
