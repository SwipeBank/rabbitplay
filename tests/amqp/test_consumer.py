import mock
import unittest
import pika
from amqp.consumer import Consumer


class TestConsumer(unittest.TestCase):
    def setUp(self):
        self._queue = 'my_queue'
        self._host = 'my_host.com'

    def tearDown(self):
        pass

    @mock.patch('amqp.consumer.get_channel')
    def test_consumer_constructor(self, mock_get_channel):
        ChannelMock = mock.Mock({
            'basic_qos.return_value': 1
        })
        mock_get_channel.return_value = (ChannelMock(), 1)
        consumer = Consumer(self._queue, host=self._host)
        mock_get_channel.assert_called_once_with(self._queue, host=self._host)
