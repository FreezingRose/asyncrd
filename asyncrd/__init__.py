from .connection import *
from .query import *

class connecter():
    def __init__(self, connection_url : str):
        self.connection_url = connection_url
      
    @classmethod
    async def connect(cls):
        cls.connection = ConnectionProtocol(connection_url)
        return cls.connection
        
    async def __aenter__(self):
        connection = await self.connect()
        return connection
    
    async def __aexit__(self, *args, **kwargs):
        await self.connection.close()
        return self

connect = connecter
