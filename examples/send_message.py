#!/usr/bin/env python

import sys
from rabbitplay import Producer


with Producer('hello_world_queue', user='user',
              password='password', vhost='vhost') as producer:
    producer.publish(' '.join(sys.argv[1:]) or 'hello')
