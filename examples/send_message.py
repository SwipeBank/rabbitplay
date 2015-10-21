#!/usr/bin/env python

import sys
from rabbitplay import Producer


with Producer(queue='hello') as producer:
    producer.publish(' '.join(sys.argv[1:]) or 'hello')
