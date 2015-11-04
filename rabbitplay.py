import pika
import ssl

__rabbit_connection__ = None


class RabbitPlay(object):

    def __init__(self, queue, host='localhost', port=5672, vhost=None,
                 user=None, password=None, clean_creds=None, channel_max=None,
                 frame_max=None, heartbeat_interval=None, ca_certs=None,
                 cert_reqs=ssl.CERT_NONE, certfile=None, keyfile=None,
                 ssl_enable=False, ssl_version=ssl.PROTOCOL_SSLv23,
                 connection_attempts=None, retry_delay=None, locale=None,
                 socket_timeout=None, backpressure_detection=None):
        self.queue = queue
        self.host = host
        self.port = port
        self.vhost = vhost
        self.user = user
        self.password = password
        self.clean_creds = clean_creds
        self.channel_max = channel_max
        self.frame_max = frame_max
        self.heartbeat_interval = heartbeat_interval
        self.ca_certs = ca_certs
        self.cert_reqs = cert_reqs
        self.certfile = certfile
        self.keyfile = keyfile
        self.ssl_enable = ssl_enable
        self.ssl_version = ssl_version
        self.connection_attempts = connection_attempts
        self.retry_delay = retry_delay
        self.locale = locale
        self.socket_timeout = socket_timeout
        self.backpressure_detection = backpressure_detection
        self._channels = {}

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self._channel.connection.close()

    def _credentials(self):
        if not self.user:
            return None
        return pika.credentials.PlainCredentials(
                username=self.user,
                password=self.password,
                erase_on_connect=self.clean_creds
            )

    def _ssl_options(self):
        if not self.ssl_enable:
            return None
        return {
            "ca_certs": self.ca_certs,
            "cert_reqs": self.cert_reqs,
            "certfile": self.certfile,
            "keyfile": self.keyfile,
            "ssl_enable": self.ssl_enable,
            "ssl_version": self.ssl_version
        }

    def _connection_params(self):
        return pika.ConnectionParameters(
            host=self.host,
            port=self.port,
            virtual_host=self.vhost,
            credentials=self._credentials(),
            channel_max=self.channel_max,
            frame_max=self.frame_max,
            heartbeat_interval=self.heartbeat_interval,
            ssl=self.ssl_enable,
            ssl_options=self._ssl_options(),
            connection_attempts=self.connection_attempts,
            retry_delay=self.retry_delay,
            locale=self.locale,
            socket_timeout=self.socket_timeout,
            backpressure_detection=self.backpressure_detection
        )

    @property
    def _connection(self):
        conn = __rabbit_connection__
        if conn and conn.is_open:
            return conn
        conn = pika.BlockingConnection(self._connection_params())
        return conn

    @property
    def _channel(self):
        channel = self._channels.get(self.queue)
        if channel and channel.is_open:
            return channel
        channel = self._connection.channel()
        channel.queue_declare(
            queue=self.queue,
            durable=True
        )
        self._channels[self.queue] = channel
        return channel


class Producer(RabbitPlay):
    def __init__(self, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        # confirm that he message has reached the queue:
        self._channel.confirm_delivery()

    def publish(self, message):
        return self._channel.basic_publish(
            exchange='',
            routing_key=self.queue,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            )
        )


class Consumer(RabbitPlay):
    def __init__(self, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        # set quality of service (qos) with prefetch count equal to 1.
        # TODO: should we try to play with this parameter?
        self._channel.basic_qos(prefetch_count=1)

    def _callback_with_ack(self, callback):
        def callback_with_ack(channel, method, properties, body):
            callback(body)
            channel.basic_ack(delivery_tag=method.delivery_tag)
        return callback_with_ack

    def subscribe(self, on_message):
        self._channel.basic_consume(
            self._callback_with_ack(on_message),
            queue=self.queue
        )
        self._channel.start_consuming()