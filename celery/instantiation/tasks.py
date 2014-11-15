from __future__ import absolute_import

from proj.celery import app

from celery import Task

class NaiveAuthenticateServer(Task):

    def __init__(self):
        self.defaul = 1

    def run(self, x):
        try:
            return x + self.defaul
        except KeyError:
            return False

add = app.tasks[NaiveAuthenticateServer.name]