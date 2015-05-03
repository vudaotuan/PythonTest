__author__ = 'tuanvu'
__create_time__ = '02/05/2015 10:34 PM'

from kafka import KafkaConsumer

# To consume messages
consumer = KafkaConsumer("truckevent",
                         group_id="my_group",
                         bootstrap_servers=["10.3.9.13:2181"])
for message in consumer:
    # message value is raw byte string -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                         message.offset, message.key,
                                         message.value))

consumer.close()