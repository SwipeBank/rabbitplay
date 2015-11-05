#!/usr/bin/env python

from rabbitplay import Producer
from rabbitplay import RabbitConnection as Connection
from time import sleep
import sys


with Connection.instance(user='user', password='password',
                         vhost='vhost') as conn:

    producer1 = Producer(conn)
    producer1.publish('queue1', 'msg1')
    producer1.publish('queue2', 'msg1')
    producer1.publish('queue2', 'msg2')

    sleep(3)

    producer2 = Producer(conn)
    producer2.publish('queue3', 'msg1')
    producer2.publish('queue4', 'msg1')
