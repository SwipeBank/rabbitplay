from msg_broker.channel import get_channel


class Consumer(object):
    """ An abstraction layer for easy messages consuming.

        Example of usage:

        def on_message(message):
            print '[x] Received "{}"'.format(message)

        with Consumer('hello_world_queue') as my_consumer:
            my_consumer.subscribe(on_message)
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
        # Set Quality Of Service (QOS) with prefetch count equal to 1.
        # TODO: Should we try to play with this parameter?
        self._channel.basic_qos(prefetch_count=1)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self._connection.close()
        print "Consumer's connection is closed."

    def _callback_with_ack(self, callback):
        def callback_with_ack(channel, method, properties, body):
            callback(body)
            channel.basic_ack(delivery_tag=method.delivery_tag)
        return callback_with_ack

    def subscribe(self, on_message):
        self._channel.basic_consume(
            self._callback_with_ack(on_message),
            queue=self._queue
        )
        self._channel.start_consuming()
