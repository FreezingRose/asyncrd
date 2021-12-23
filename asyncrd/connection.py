import asyncio, socket
from urllib.parse import urlparse
from .query import Query, Get, Set, BasicProtocol
from .exceptions import RedisException

class ConnectionProtocol():
    def __init__(self, connection_url : str):
        self.connection_url = urlparse(connection_url)
        self.hostname = self.connection_url.hostname
        self.port = self.connection_url.port
        
        self.reader = None
        self.writer = None
        
        self._closed = False
        
    async def connect(self):
        self.reader, self.writer = await asyncio.open_connection(self.hostname, self.port)
        
    async def close(self):
        if self._closed:
            raise RedisException('Connection is closed.')
            
        self.writer.close()
        await self.writer.wait_closed()
        self._closed = True
        
    async def __aenter__(self):
        await self.connect()
        return self
    
    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.close()
        
    async def get(self, query : str):
        data = Query(self)
        result = await data.do_query(Get(query=query))
        return result

    async def set(self, query : str):
        data = Query(self)
        result = await data.do_query(Set(query=query))
        return result
