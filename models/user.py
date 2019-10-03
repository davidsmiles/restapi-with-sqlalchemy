from dbconn import Database


class UserModel:
    TABLE_NAME = 'users'
    DB_NAME = 'data.db'

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        with Database(cls.DB_NAME) as connection:
            cursor = connection.cursor()
            query = 'SELECT * FROM {} WHERE username = ?'.format(cls.TABLE_NAME)
            result = cursor.execute(query, (username,))
            user = result.fetchone()

        return cls(*user) if user else None

    @classmethod
    def find_by_id(cls, user_id):
        with Database(cls.DB_NAME) as connection:
            cursor = connection.cursor()
            query = 'SELECT * FROM {} WHERE id = ?'.format(cls.TABLE_NAME)
            result = cursor.execute(query, (user_id,))
            user = result.fetchone()

        return cls(*user) if user else None


