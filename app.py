from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity

from datetime import timedelta

from resources.user import UserRegister
from resources.item import *

app = Flask(__name__)
app.secret_key = 'david'
api = Api(app)

app.config['JWT_AUTH_URL_RULE'] = '/login'
jwt = JWT(app, authenticate, identity)
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
app.config['JWT_AUTH_USERNAME_KEY'] = 'username'

@jwt.auth_request_handler
def customized_response_handler(access_token, identity):
    return jsonify({
        'token': access_token.decode('utf-8'),
        'userid': identity.id
    })


api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister, '/signup')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
