#!/usr/bin/env python

from rabbitplay import Producer
from rabbitplay import RabbitConnection as Connection
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('queue', nargs='?', default='hello_world_queue')
parser.add_argument('message', default='Hello World!')
args = parser.parse_args()

with Connection.instance(user='user', password='password',
                         vhost='vhost') as conn:

    print 'queue:   {}\nmessage: {}'.format(args.queue, args.message)
    producer1 = Producer(conn)
    producer1.publish(args.queue, args.message)
