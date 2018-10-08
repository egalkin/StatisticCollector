from flask_restful import Resource, abort
import pygal

from collector import collector_parser, plots_info


class Collector(Resource):
    def post(self):
        args = collector_parser.parse_args()
        nums_of_responses = args['num_of_responses']
        status = args['status']
        last_mod = args['last_mod']
        url = args['url']
        if status == 'create':
            plots_info[url] = [int(nums_of_responses)]
        elif status == 'update':
            plots_info[url].append(int(nums_of_responses))
        else:
            abort(406, message='No such status \'{}\' for collector'.format(status))
        return 200


class PlotBuilder(Resource):
    def post(self):
        args = collector_parser.parse_args()
        url = args['url']
        line_chart = pygal.Line()
        line_chart.title = 'Num of responses statistic'
        line_chart.x_label = map(str, range(1, len(plots_info[url]) + 1))
        line_chart.add('Trend line', plots_info[url])
        return line_chart.render_response()