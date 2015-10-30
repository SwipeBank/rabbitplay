# RabbitPlay

Abstraction on top of [pika](https://pika.readthedocs.org/) library for working with [RabbitMQ](https://www.rabbitmq.com/).

## Examples  

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
