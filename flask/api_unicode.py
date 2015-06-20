# -*- coding: utf-8 -*-
__author__ = 'tuanvu'
__create_time__ = '23/05/2015 12:22 PM'

import json
from flask import request, make_response
from flask.ext import restful
from flask import Flask, make_response

class ActivityReportService(restful.Resource):
    def get(self):
        data = {'name': "Vũ đẹp zai"}

        response = json.dumps(data)
        return make_response(response)
