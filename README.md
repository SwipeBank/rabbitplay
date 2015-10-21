# RabbitPlay

A simple abstraction on top of python [pika](https://pika.readthedocs.org/) to deal with [RabbitMQ](https://www.rabbitmq.com/).

## Examples  

### Consumer:  

```sh
python -m examples.receive
```  

### Producer:  

```sh
python -m examples.send_message 'rabbit1...............'
python -m examples.send_message 'rabbit2..........'
python -m examples.send_message 'rabbit3.....'
```
