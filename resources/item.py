from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from dbconn import Database
from models.item import ItemModel

class Item(Resource):
    DB_NAME = 'items.db'
    TABLE_NAME = 'items'

    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field cannot be left blank')

    def get(self, name):
        item = ItemModel.find_by_name(name)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            error_msg = {'message': f'item with name {name} already exists'}
            return error_msg, 400

        data = Item.parser.parse_args()
        price = data['price']

        try:
            return ItemModel.insert(name, price), 201
        except:
            return {'message': 'internal server error'}, 500

    def delete(self, name):
        if ItemModel.find_by_name(name):
            with Database(self.DB_NAME) as connection:
                cursor = connection.cursor()
                query = 'DELETE FROM {} WHERE name = ?'.format(self.TABLE_NAME)
                result = cursor.execute(query, (name,))
                return {'message': 'item deleted'}, 200
        else:
            return {'message': f'no item with name {name} in database'}, 301

    def put(self, name):
        data = Item.parser.parse_args()
        price = data['price']

        if ItemModel.find_by_name(name):    # if exists, then update
            ItemModel.update(name, price)
        else:
            ItemModel.insert(name, price)   # else update data

        return {'message': 'item has been put'}, 200


class ItemList(Resource):

    @jwt_required()
    def get(self):
        with Database(Item.DB_NAME) as connection:
            cursor = connection.cursor()
            query = 'SELECT * FROM {}'.format(Item.TABLE_NAME)
            result = cursor.execute(query)
            items = [ItemModel(*row).json() for row in result.fetchall()]

        response = {'items': items}
        return response, 200
