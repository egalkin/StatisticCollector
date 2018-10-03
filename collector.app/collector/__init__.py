from collector.api_folder.collecotr_api import Collector, PlotBuilder
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app, prefix='/api/v1')
