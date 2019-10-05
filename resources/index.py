from flask_restful import Resource, reqparse


class Index(Resource):

    def get(self):
        return {
            'message': 'welcome to the stores-rest-api'
        }