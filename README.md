# RabbitPlay

Abstraction on top of [pika](https://pika.readthedocs.org/) library for working with [RabbitMQ](https://www.rabbitmq.com/).

## Installation

* Using [pip](https://pip.readthedocs.org/en/stable/):
  ```sh
  # master branch:
  pip install git+https://github.com/SwipeBank/rabbitplay.git#egg=rabbitplay
  # specific version (tag):
  pip install git+https://github.com/SwipeBank/rabbitplay.git@0.7#egg=rebbitplay-0.7
  ```

* Manual installation:
  ```sh
  git clone https://github.com/SwipeBank/rabbitplay.git
  cd rabbitplay
  # git checkout 0.7
  python setup.py install
  ```

## Examples  

Examples are configured to use a default user `user`, password `password` and virtual host `vhost`.

*Hint:  
You can use Docker Compose to launch a RabbitMQ instance with required settings.*

### Consumer:  

* [Command line](/examples/receive.py):
  ```sh
  # hello_world_queue:
  python -m examples.receive
  # custom queue:
  python -m examples.receive 'my_queue'
  ```


### Producer:  

* [Custom queue \ message](/examples/send_message.py):
  ```sh
  python -m examples.send_message 'queue1' 'rabbit1.'
  python -m examples.send_message 'queue1' 'rabbit5.....'
  python -m examples.send_message 'message_to_default_queue'
  ```


* [Multiple messages \ queues](/examples/send_messages.py):
  ```sh
  python -m examples.send_messages
  ```
