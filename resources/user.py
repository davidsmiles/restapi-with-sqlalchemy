from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        help='This field should not be left blank',
                        required=True)

    parser.add_argument('password',
                        type=str,
                        help='This field should not be left blank',
                        required=True)

    def post(self):
        data = UserRegister.parser.parse_args()
        username = data['username']
        password = data['password']

        user = UserModel.find_by_username(username)
        if not user:
            user = UserModel(**data)
            user.add_to_db()
            return {'message': 'successfully created'}

        return {'message': 'user already exists'}


class User(Resource):
    @classmethod
    def get(cls, username):
        user = UserModel.find_by_username(username)
        if not user:
            return {'message': 'user not found.'}, 404
        return user.json()

    @classmethod
    def delete(cls, username):
        user = UserModel.find_by_username(username)
        if not user:
            return {'message': 'user not found.'}, 404

        user.delete()
        return {'message': 'user has been deleted'}


class UsersList(Resource):
    def get(self):
        return [user.json() for user in UserModel.find_all()]