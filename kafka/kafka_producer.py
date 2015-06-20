# -*- coding: utf-8 -*-
__author__ = 'tuanvu'
__create_time__ = '02/05/2015 10:07 PM'

from kafka import SimpleProducer, KafkaClient

# To send messages synchronously
kafka = KafkaClient("10.3.9.13:6667")
producer = SimpleProducer(kafka)

# Note that the application is responsible for encoding messages to type str
producer.send_messages("truckevent", "some message")
producer.send_messages("truckevent", "this method", "is variadic")

# To send messages asynchronously
# WARNING: current implementation does not guarantee message delivery on failure!
# messages can get dropped! Use at your own risk! Or help us improve with a PR!
producer = SimpleProducer(kafka, async=True)
producer.send_messages("truckevent", "async message")

# To wait for acknowledgements
# ACK_AFTER_LOCAL_WRITE : server will wait till the data is written to
#                         a local log before sending response
# ACK_AFTER_CLUSTER_COMMIT : server will block until the message is committed
#                            by all in sync replicas before sending a response
producer = SimpleProducer(kafka, async=False,
                          req_acks=SimpleProducer.ACK_AFTER_LOCAL_WRITE,
                          ack_timeout=2000)

response = producer.send_messages("truckevent", "another message")

if response:
    print(response[0].error)
    print(response[0].offset)

# To send messages in batch. You can use any of the available
# producers for doing this. The following producer will collect
# messages in batch and send them to Kafka after 20 messages are
# collected or every 60 seconds
# Notes:
# * If the producer dies before the messages are sent, there will be losses
# * Call producer.stop() to send the messages and cleanup
producer = SimpleProducer(kafka, batch_send=True,
                          batch_send_every_n=20,
                          batch_send_every_t=60)