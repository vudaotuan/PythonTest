# -*- coding: utf-8 -*-
__author__ = 'tuanvu'
__create_time__ = '23/05/2015 12:21 PM'

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from flask import Flask
from flask.ext.restful import Api
from flask.ext.restful.representations.json import output_json

output_json.func_globals['settings'] = {'ensure_ascii': False, 'encoding': 'utf8'}
app = Flask(__name__)
api = Api(app)

from api_unicode import ActivityReportService

api.add_resource(ActivityReportService, '/api/v1/apikey')

app.run(debug=True, host='0.0.0.0', port=9898)
