import asyncio, socket
from urllib.parse import 
from .query import Query

class ConnectionProtocol():
    def __init__(self, connection_url : str):
        self.connection_url = urlparse(connection_url)
        self.hostname = self.connection_url.hostname
        self.port = self.connection_url.port
        
    async def connect(self):
        self.connection = await asyncio.open_connection(self.hostname, self.port)
    
