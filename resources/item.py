from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field cannot be left blank')

    def get(self, name):
        item = ItemModel.find_by_name(name)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            error_msg = {'message': f'item with name {name} already exists'}
            return error_msg, 400

        data = Item.parser.parse_args()
        price = data['price']

        item = ItemModel(name, price)
        try:
            item.upsert()
            return item.json()
        except:
            return {'message': 'internal server error'}, 500

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete()
            return item.json()
        return {'message': f'no item with name {name} in database'}, 200

    def put(self, name):
        data = Item.parser.parse_args()
        price = data['price']

        item = ItemModel.find_by_name(name)
        if not item:                            # if dont exists, then add
            item = ItemModel(name, price)
        else:
            item.price = price                  # else update data

        item.upsert()

        return {'message': 'item has been put'}, 200


class ItemList(Resource):

    @jwt_required()
    def get(self):
        items = ItemModel.query.all()
        items = [item.json() for item in items]

        response = {'items': items}
        return response, 200
