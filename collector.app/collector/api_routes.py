from collector import api, app
from collector.collector_api import Collector, PlotBuilder

api.add_resource(Collector, '/collect')
api.add_resource(PlotBuilder, '/plot')

if __name__ == '__main__':
    app.run()
