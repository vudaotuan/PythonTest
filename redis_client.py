import redis

POOL = redis.ConnectionPool(host='10.3.9.28', port=6379, db=0)

my_server = redis.Redis(connection_pool=POOL)

print len(my_server.keys("*"))