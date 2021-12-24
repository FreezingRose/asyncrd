from .connection import *
from .query import *

class connecter():
    def __init__(self, connection_url : str):
        self.connection_url = connection_url
        self.connection = ConnectionProtocol(connection_url)
        
    async def __aenter__(self):
        await self.connection.connect()
        return self.connection
    
    async def __aexit__(self, *args, **kwargs):
        await self.connection.close()
        return self

connect = connecter()
