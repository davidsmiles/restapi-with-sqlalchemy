from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()

        return {'message': 'store not found'}, 404

    def post(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return {'message': f'store with {name} already exists'}

        store = StoreModel(name)
        try:
            store.insert()
        except:
            return {'message': 'internal serval error'}, 500

        return store.json()

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete()
        return {'message': 'store deleted'}


class StoreList(Resource):

    def get(self):
        return {
            'stores': [store.json() for store in StoreModel.find_all()]
        }

    def delete(self):
        StoreModel.delete_all()
        return {'message': 'all deleted'}