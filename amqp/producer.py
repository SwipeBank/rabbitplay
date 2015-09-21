from msg_broker.channel import get_channel, publish_properties


class Producer(object):
    """ An abstraction layer for easy message publishing.

        Example of usage:

        with Producer('hello_world_queue') as my_producer:
            is_published = my_producer.publish(
                json_dumps({'name': 'Bob', age': 42})
            )
    """

    def __init__(self, queue, host='localhost', port=None, vhost=None,
                 user=None, password=None, clean_creds=True):
        self._queue = queue
        self._host = host
        self._port = port
        self._vhost = vhost
        self._user = user
        self._password = password
        self._clean_creds = clean_creds
        self._channel, self._connection = get_channel(
            self._queue,
            host=self._host,
            port=self._port,
            vhost=self._vhost,
            user=self._user,
            password=self._password,
            clean_creds=self._clean_creds
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
