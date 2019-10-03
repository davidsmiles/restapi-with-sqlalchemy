from dbconn import Database

class ItemModel:
    DB_NAME = 'items.db'
    TABLE_NAME = 'items'

    def __init__(self, _id, name, price):
        self.id = _id
        self.name = name
        self.price = price

    def json(self):
        return {
                'id': self.id,
                'name': self.name,
                'price': self.price
            }

    @classmethod
    def find_by_name(cls, name):
        with Database(cls.DB_NAME) as connection:
            cursor = connection.cursor()
            query = 'SELECT * FROM {} WHERE name = ?'.format(cls.TABLE_NAME)
            result = cursor.execute(query, (name,))
            item = result.fetchone()
        return ItemModel(*item) if item else None

    @classmethod
    def insert(cls, name, price):
        with Database(cls.DB_NAME) as connection:
            cursor = connection.cursor()
            insert_time = 'INSERT INTO {} VALUES(NULL, ?, ?)'.format(cls.TABLE_NAME)
            cursor.execute(insert_time, (name, price))
        return ItemModel(cls.find_by_name(name).id, name, price).json()

    @classmethod
    def update(cls, name, price):
        with Database(cls.DB_NAME) as connection:
            cursor = connection.cursor()
            query = 'UPDATE {} SET price = ? WHERE name = ?'.format(cls.TABLE_NAME)
            cursor.execute(query, (price, name))
