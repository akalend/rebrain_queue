#!/usr/bin/env python
import pika, sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

message = '111222333!'
if len(sys.argv) > 1:
    message = sys.argv[1]

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)
print(message)

connection.close()
