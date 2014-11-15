from __future__ import absolute_import

from custom_class.celery import app


class _AddTask(app.Task):

    def run(self, x, y):
        return x + y
add = app.tasks[_AddTask.name]