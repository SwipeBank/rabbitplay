from msg_broker.channel import get_channel, publish_properties
import ssl


class Producer(object):
    """ An abstraction layer for easy message publishing.

        Example of usage:

        with Producer('hello_world_queue') as my_producer:
            is_published = my_producer.publish(
                json_dumps({'name': 'Bob', age': 42})
            )
    """

    def __init__(self, queue, host='localhost', port=None, vhost=None,
                 user=None, password=None, clean_creds=True,
                 heartbeat_interval=30, ca_certs=None, cert_reqs=ssl.CERT_NONE,
                 certfile=None, keyfile=None, ssl_enable=False,
                 ssl_version=ssl.PROTOCOL_SSLv23):
        self._queue = queue
        self._channel, self._connection = get_channel(
            self._queue,
            host=host,
            port=port,
            vhost=vhost,
            user=user,
            password=password,
            clean_creds=clean_creds,
            heartbeat_interval=heartbeat_interval,
            ca_certs=ca_certs,
            cert_reqs=cert_reqs,
            certfile=certfile,
            keyfile=keyfile,
            ssl_enable=ssl_enable,
            ssl_version=ssl_version
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
