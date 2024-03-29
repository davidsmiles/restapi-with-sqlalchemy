import os

from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity

from datetime import timedelta

from resources.index import Index
from resources.user import *
from resources.item import *
from resources.store import *

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
db_uri = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'david'
api = Api(app)

app.config['JWT_AUTH_URL_RULE'] = '/login'
jwt = JWT(app, authenticate, identity)
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
app.config['JWT_AUTH_USERNAME_KEY'] = 'username'

api.add_resource(Index, '/')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(User, '/user/<string:username>')
api.add_resource(UserRegister, '/signup')
api.add_resource(UsersList, '/users')


if __name__ == '__main__':
    from DB import DB
    DB.init_app(app)

    app.run(port=5000, debug=True)
