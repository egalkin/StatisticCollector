from collector import api, app
from collector.api_folder.collecotr_api import Collector, PlotBuilder

api.add_resource(Collector, '/collect')
api.add_resource(PlotBuilder, '/plot')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
