# RabbitPlay

Abstraction on top of [pika](https://pika.readthedocs.org/) library for working with [RabbitMQ](https://www.rabbitmq.com/).

## Examples  

Examples are configured to use a default user `user`, password `password` and virtual host `vhost`.

*Hint:  
You can use Docker Compose to launch a RabbitMQ instance with required settings.*

### Consumer:  

```sh
python -m examples.receive
```  

### Producer:  

```sh
python -m examples.send_message 'rabbit1.'
python -m examples.send_message 'rabbit5.....'
python -m examples.send_message 'rabbit10..........'
```
