#!/usr/bin/env python

import sys
from flask_rabbitplay.rabbitplay import Producer

# vhost:
#   vhost='vhost', user='user', password='password'
# ssl:
#   ssl_enable=True, certfile='/path/to/cert.pem', keyfile='/path/to/key.pem'
with Producer('hello_world_queue') as producer:
    producer.publish(' '.join(sys.argv[1:]) or 'Hello World!')
