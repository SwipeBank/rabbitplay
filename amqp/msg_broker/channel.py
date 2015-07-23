import pika


publish_properties = pika.BasicProperties(
    delivery_mode=2,    # make message persistent
)


def _get_connection(host='localhost'):
    return pika.BlockingConnection(pika.ConnectionParameters(host=host))


def get_channel(queue, host='localhost'):
    """ Returns channel and connection:
    1. a new instance of channel on the host `host` with
    declaring the queue `queue`;
    2. A connection used to created a channel.
    """
    connection = _get_connection(host=host)
    channel = connection.channel()
    channel.queue_declare(queue=queue, durable=True)
    return channel, connection
