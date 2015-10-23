#!/usr/bin/env python

import sys
import time
import signal
from rabbitplay import Consumer


def signal_handler(signum, frame):
    print '\nsignal {}'.format(signum)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


with Consumer('hello_world_queue', user='user',
              password='password', vhost='vhost') as consumer:
    def on_message(msg):
        print '[x] received "{}"'.format(msg)
        time.sleep(msg.count('.'))
        print '[x] done'
    consumer.subscribe(on_message)
