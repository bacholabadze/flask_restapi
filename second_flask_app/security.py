from user import User

users = [
    User(1, 'bob', '1234')
]

username_mapping = {user1.username: user1 for user1 in users}

userid_mapping = {user1.id: user1 for user1 in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
    print(user_id)
    print(payload)
    return userid_mapping.get(user_id, None)
