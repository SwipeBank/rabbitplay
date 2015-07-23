from amqp.msg_broker import channel
import unittest
import mock


class TestChannel(unittest.TestCase):
    def setUp(self):
        self._host = 'my_host.com'
        self._port = '5672'
        self._queue = 'my_queue'

    def tearDown(self):
        pass

    @mock.patch('amqp.msg_broker.channel.pika')
    def test_get_connection(self, mock_pika):
        mock_pika.BlockingConnection.return_value = 42
        connection = channel._get_connection(host=self._host)
        mock_pika.BlockingConnection.assert_called_with(
            mock_pika.ConnectionParameters(host=self._host)
        )
        self.assertEquals(connection, 42)

    @mock.patch('amqp.msg_broker.channel._get_connection')
    def test_get_channel(self, mock_get_connection):
        ch, connection = channel.get_channel(
            self._queue,
            host=self._host,
            port=self._port
        )
        mock_get_connection.assert_called_with(
            host=self._host,
            port=self._port
        )
