__author__ = 'tuanvu'
__create_time__ = '25/05/2015 11:08 PM'

import redis

REDIS_CONN_POOL = redis.ConnectionPool(host="cache.goku.me", port=6379, db=1,
                                       password='ca5roh6aejaz0kiQuieh7iaroo7aedaP')
f = open('template_mail.txt', 'r')
for line in f:
    template = line
    print template

redis_client = redis.Redis(connection_pool=REDIS_CONN_POOL)

redis_client.set("template123231", template)
