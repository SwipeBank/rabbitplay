# RabbitPlay

Abstraction on top of [pika](https://pika.readthedocs.org/) library for working with [RabbitMQ](https://www.rabbitmq.com/).

## Examples  

Examples are configured to use a default user `user`, password `password` and virtual host `vhost`.

*Hint:  
You can use Docker Compose to launch a RabbitMQ instance with required settings.*

### Consumer:  

```sh
python -m examples.receive
python -m examples.receive 'my_queue'
```  

### Producer:  

Custom queue \ message:
```sh
python -m examples.send_message 'queue1' 'rabbit1.'
python -m examples.send_message 'queue1' 'rabbit5.....'
python -m examples.send_message 'queue1' 'rabbit10..........'
python -m examples.send_message 'queue2' 'rabbit_feet'
python -m examples.send_message 'message_to_default_queue'
```

Multiple messages \ queues:
```sh
python -m examples.send_messages
```
