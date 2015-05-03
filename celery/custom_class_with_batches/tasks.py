from __future__ import absolute_import

from custom_class_with_batches.celery import app
from celery.contrib.batches import Batches


class _AddTask(Batches):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.flush_every = 5
        self.flush_interval = 5

        self.logger.info("Finish init send batch mail job")

    def run(self, items):
        print [item.kwargs for item in items]
        return 1
add = app.tasks[_AddTask.name]