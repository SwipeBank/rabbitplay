#!/usr/bin/env python

import sys
import time
import signal
from flask_rabbitplay.rabbitplay import Consumer


def signal_handler(signum):
    print '\nSignal {}'.format(signum)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# vhost:
#   vhost='vhost', user='user', password='password'
# ssl:
#   ssl_enable=True, certfile='/path/to/cert.pem', keyfile='/path/to/key.pem'
with Consumer('hello_world_queue') as consumer:
    def on_message(msg):
        print '[x] Received "{}"'.format(msg)
        time.sleep(msg.count('.'))
        print '[x] Done'
    consumer.subscribe(on_message)
