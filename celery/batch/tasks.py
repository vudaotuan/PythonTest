__author__ = 'Administrator'
from celery.contrib.batches import Batches
from celery import Celery

app = Celery('tasks', broker='amqp://guest:guest@localhost:5672//')

@app.task(base=Batches, flush_every=5, flush_interval=10)
def add(items):
	total = 0
	for x in items:
		total = total + x

    print('>>> Total: {0}'.format(total))
    return total