
import socket

DEFAULT_HOST = 'cloudtee.me'
DEFAULT_PORT = '8080'


class Stream(object):
    def __init__(self, host, port, topic):
        self.conn_info = (host, port)
        self.topic = topic
        self.socket = self._connect()

    def _connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(self.conn_info)
        init_message = 'SEND %s\n' % self.topic
        sock.send(init_message)
        return sock

    def send(self, data):
        self.socket.send(data)


def connect(topic, host=DEFAULT_HOST, port=DEFAULT_PORT):
    return Stream(host, port, topic)
