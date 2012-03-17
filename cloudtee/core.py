
import socket


class _Stream(object):
    def __init__(self, host, port, topic):
        self.conn_info = (host, port)
        self.topic = topic
        self.socket = self._open_socket()

        self._init_socket(self.socket, topic)

    def _init_socket(self, socket):
        raise NotImplementedError()

    def _open_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(self.conn_info)
        return sock

    def close(self):
        self.socket.close()


class WritableStream(_Stream):
    def _init_socket(self, sock, topic):
        init_message = 'SEND %s\n' % topic
        sock.send(init_message)

    def write(self, data):
        self.socket.send(data)


class ReadableStream(_Stream):
    def _init_socket(self, sock, topic):
        init_message = 'GET /%s\r\n\r\n' % topic
        sock.send(init_message)

    def read(self):
        while True:
            yield self.socket.recv(1024)
