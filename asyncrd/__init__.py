from .connection import *
from .query import *

async def connect(connection_url):
    connection = ConnectionProtocol(connection_url)
    cls = connection
    return cls
