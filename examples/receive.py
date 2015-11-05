#!/usr/bin/env python

from rabbitplay import Consumer
from rabbitplay import RabbitConnection as Connection
import argparse
import signal
import sys
import time

parser = argparse.ArgumentParser()
parser.add_argument('queue', nargs='?', default='hello_world_queue')
args = parser.parse_args()


def signal_handler(signum, frame):
    print '\nsignal {}'.format(signum)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


with Connection.instance(user='user', password='password',
                         vhost='vhost') as conn:
    def on_message(msg):
        print '[x] received "{}"'.format(msg)
        time.sleep(msg.count('.'))
        print '[x] done'

    consumer1 = Consumer(conn)
    print 'queue: {}\nlistening...'.format(args.queue)
    consumer1.subscribe('queue1', on_message)
