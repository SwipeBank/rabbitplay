#!/usr/bin/env python

from rabbitplay import Consumer
from rabbitplay import RabbitConnection as Connection
import signal
import sys
import time


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
    consumer1.subscribe('queue1', on_message)
