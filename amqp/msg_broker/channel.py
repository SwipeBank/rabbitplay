import pika
import ssl


publish_properties = pika.BasicProperties(
    delivery_mode=2,    # make message persistent
)


def set_broker_credentials(user=None, password=None, clean_creds=True):
    if not user:
        return None
    return pika.credentials.PlainCredentials(
        username=user,
        password=password,
        erase_on_connect=clean_creds
    )


def set_broker_ssl(ssl_enable=False, **kwargs):
    if not ssl_enable or not kwargs:
        return None
    ssl_options = {}
    for key, value in kwargs.iteritems():
        ssl_options[key] = value
    return ssl_options


def _get_connection(**kwargs):
    broker_credentials = set_broker_credentials(
        user=kwargs['user'],
        password=kwargs['password'],
        clean_creds=kwargs['clean_creds']
    )
    broker_ssl = set_broker_ssl(
        ca_certs=kwargs['ca_certs'],
        cert_reqs=kwargs['cert_reqs'],
        certfile=kwargs['certfile'],
        keyfile=kwargs['keyfile'],
        ssl_enable=kwargs['ssl_enable'],
        ssl_version=kwargs['ssl_version']
    )
    return pika.BlockingConnection(
        pika.ConnectionParameters(
            host=kwargs['host'],
            port=kwargs['port'],
            virtual_host=kwargs['vhost'],
            credentials=broker_credentials,
            ssl=kwargs['ssl_enable'],
            ssl_options=broker_ssl
        )
    )


def get_channel(queue, host='localhost', port=None, vhost=None,
                user=None, password=None, clean_creds=True,
                ca_certs=None, cert_reqs=ssl.CERT_NONE, certfile=None,
                keyfile=None, ssl_enable=False, ssl_version=None):
    """ Returns channel and connection:
    1. a new instance of channel on the host `host` with
    declaring the queue `queue`;
    2. A connection used to created a channel.
    """
    connection = _get_connection(
        host=host,
        port=port,
        vhost=vhost,
        user=user,
        password=password,
        clean_creds=clean_creds,
        ca_certs=ca_certs,
        cert_reqs=cert_reqs,
        certfile=certfile,
        keyfile=keyfile,
        ssl_enable=ssl_enable,
        ssl_version=ssl_version
    )
    channel = connection.channel()
    channel.queue_declare(queue=queue, durable=True)
    return channel, connection
