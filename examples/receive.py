import sys
import time
import signal
from amqp.consumer import Consumer


def signal_handler(signum, frame):
    print '\nSignal {}'.format(signum)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

with Consumer('hello_world_queue') as consumer:
    def on_message(msg):
        print '[x] Received "{}"'.format(msg)
        time.sleep(msg.count('.'))
        print '[x] Done'
    consumer.subscribe(on_message)
    # try:
    #     consumer.subscribe(on_message)
    # except KeyboardInterrupt:
    #     print '\b\bBye.'
