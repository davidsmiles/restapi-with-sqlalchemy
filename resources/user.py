from flask_restful import Resource, reqparse
from dbconn import Database
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
            with Database(UserModel.DB_NAME) as connection:
                cursor = connection.cursor()
                signup = 'INSERT INTO {} VALUES(NULL, ?, ?)'.format(UserModel.TABLE_NAME)
                cursor.execute(signup, (username, password))
                return {'message': 'successfully created'}
        else:
            return {'message': 'user already exists'}
