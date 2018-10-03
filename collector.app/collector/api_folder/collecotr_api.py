from flask_restful import reqparse, Resource
import pygal

collector_args = ['url', 'num_of_responses', 'last_mod', 'status']
plots_info = dict()

parser = reqparse.RequestParser()

for arg in collector_args:
    parser.add_argument(arg)


class Collector(Resource):
    def get(self):
        return "hello world", 200

    def post(self):
        args = parser.parse_args()
        nums_of_responses = args['num_of_responses']
        status = args['status']
        last_mod = args['last_mod']
        url = args['url']
        if status == 'create':
            plots_info[url] = [int(nums_of_responses)]
        if status == 'update':
            plots_info[url].append(int(nums_of_responses))
        return 200


class PlotBuilder(Resource):
    def post(self):
        args = parser.parse_args()
        url = args['url']
        print(url)
        line_chart = pygal.Line()
        line_chart.title = 'Num of responses statistic'
        line_chart.x_label = map(str, range(1, len(plots_info[url]) + 1))
        line_chart.add('Trend line', plots_info[url])
        return line_chart.render_response()
