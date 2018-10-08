from flask import Flask
from flask_restful import Api, reqparse

app = Flask(__name__)
api = Api(app, prefix='/api/v1')

collector_args = ['url', 'num_of_responses', 'last_mod', 'status']
plots_info = dict()
collector_parser = reqparse.RequestParser()
for arg in collector_args:
    collector_parser.add_argument(arg)


from collector import api_routes
