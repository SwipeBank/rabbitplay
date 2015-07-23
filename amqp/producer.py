import pika
from msg_broker.channel import get_channel, publish_properties


class Producer(object):
    """ An abstraction layer for easy message publishing.

        Example of usage:

        with Producer('hello_world_queue') as my_producer:
            is_published = my_producer.publish(
                json_dumps({'name': 'Bob', age': 42})
            )
    """

    def __init__(self, queue, host='localhost'):
        self._queue = queue
        self._host = host
        self._channel, self._connection = get_channel(
            self._queue,
            host=self._host
        )
        # Message Broker should confirm that
        # the message has reached the queue:
        self._channel.confirm_delivery()

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self._connection.close()

    def publish(self, message):
        """ Returns True if the the `message` has been to the queue
        successfully.
        """
        return self._channel.basic_publish(
            exchange='',
            routing_key=self._queue,
            body=message,
            properties=publish_properties
        )