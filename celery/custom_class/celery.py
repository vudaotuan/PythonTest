from __future__ import absolute_import

from celery import Celery

app = Celery('custom_class',
             broker='amqp://guest:guest@localhost:5672//',
             include=['custom_class.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

if __name__ == '__main__':
    app.start()