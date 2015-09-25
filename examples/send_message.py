#!/usr/bin/env python

import sys
from amqp.producer import Producer

vhost = 'rabbit_host'
user = 'rabbit_user'
password = 'rabbit_password'

with Producer('hello_world_queue', vhost=vhost,
              user=user, password=password) as producer:
    producer.publish(' '.join(sys.argv[1:]) or 'Hello World!')
