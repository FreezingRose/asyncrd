import asyncio, typing
from .exceptions import CatchException, RedisException
from .parser import Parser

class Result():
    def __init__(self, result : str):
        self.result : str = result          
    
class BasicProtocol():    
    def __init__(self, query : str):
        self.query : str = query

class Set(BasicProtocol):
    command = 'SET'
            
class Get(BasicProtocol):
    command = 'GET'

class Query():
    def __init__(self, connection):
        self.reader = connection.reader
        self.writer = connection.writer
        
    async def _execute_command(self, command: str, query : str):
        parser = Parser()
        data_ = await parser.encode(command, query)
        self.writer.write(data_)
        await self.writer.drain()
        data = await self.reader.read(4096)
        print(data)
        res = await parser.decode(data)
        print(res)
        catching = CatchException(text=res)
        catched = await catching.catch_error()
        return catched
        
    async def do_query(self, protocol : typing.Union[Get, Set, BasicProtocol]):
        command = getattr(protocol, 'command', None)
        res = await self._execute_command(command, protocol.query)
        res[0] = ""
        return res
    
