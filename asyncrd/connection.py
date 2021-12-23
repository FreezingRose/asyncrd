import asyncio, socket
from urllib.parse import urlparse
from .query import Query, Get, Set
from .exceptions import RedisException

class ConnectionProtocol():
    def __init__(self, connection_url : str):
        self.connection_url = urlparse(connection_url)
        self.hostname = self.connection_url.hostname
        self.port = self.connection_url.port
        
    async def connect(self):
        self.reader, self.writer = await asyncio.open_connection(self.hostname, self.port)
        
    async def close(self):
        data = Query(self)
        await data.do_query(BasicProtocol(query="QUIT"))
        self.writer.close()
        await self.writer.wait_closed()
        
    async def get(self, query : str):
        data = Query(self)
        result = await data.do_query(Get(query=query))
        return result

    async def set(self, query : str):
        data = Query(self)
        result = await data.do_query(Set(query=query))
        return result
