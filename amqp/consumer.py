from msg_broker.channel import get_channel
import ssl


class Consumer(object):
    """ An abstraction layer for easy messages consuming.

        Example of usage:

        def on_message(message):
            print '[x] Received "{}"'.format(message)

        with Consumer('hello_world_queue') as my_consumer:
            my_consumer.subscribe(on_message)
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
