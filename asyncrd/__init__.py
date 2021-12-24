from .connection import *
from .query import *
from contextlib import asynccontextmanager

@asynccontextmanager
async def connect(connection_url : str):
    CONNECTION = ConnectionProtocol(connection_url)
    await CONNECTION.connect()
    return CONNECTION
