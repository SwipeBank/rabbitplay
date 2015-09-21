import pika


publish_properties = pika.BasicProperties(
    delivery_mode=2,    # make message persistent
)


def broker_credentials(user=None, password=None, clean_creds=True):
    if not user:
        return None
    return pika.credentials.PlainCredentials(
        username=user,
        password=password,
        erase_on_connect=clean_creds
    )


def _get_connection(host='localhost', port=None, vhost=None,
                    user=None, password=None, clean_creds=True):
    return pika.BlockingConnection(
        pika.ConnectionParameters(
            host=host,
            port=port,
            virtual_host=vhost,
            credentials=broker_credentials(
                user=user,
                password=password,
                clean_creds=clean_creds
            )
        )
    )


def get_channel(queue, host='localhost', port=None, vhost=None,
                user=None, password=None, clean_creds=True):
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
        clean_creds=clean_creds
    )
    channel = connection.channel()
    channel.queue_declare(queue=queue, durable=True)
    return channel, connection
