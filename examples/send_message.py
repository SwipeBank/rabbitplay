#!/usr/bin/env python

import sys
from amqp.producer import Producer

with Producer('hello_world_queue') as producer:
    producer.publish(' '.join(sys.argv[1:]) or 'Hello World!')
