import sys
import time
import signal
from amqp.consumer import Consumer


def signal_handler(signum, frame):
    print '\nSignal {}'.format(signum)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

vhost = 'rabbit_host'
user = 'rabbit_user'
password = 'rabbit_password'

with Consumer('hello_world_queue', vhost=vhost,
              user=user, password=password) as consumer:
    def on_message(msg):
        print '[x] Received "{}"'.format(msg)
        time.sleep(msg.count('.'))
        print '[x] Done'
    consumer.subscribe(on_message)
