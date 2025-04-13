import logging
import asyncio

logger = logging.getLogger(__name__)

class SerialProtocol(asyncio.Protocol):
    def __init__(self, port, app):
        self.port = port
        self.buffer = ''
        app['messages'][self.port] = []
        self.app = app
    
    
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        line = data.decode().strip()
        logger.info(f"[{self.port}] {line}")
        self.app['messages'][self.port].append(line)
