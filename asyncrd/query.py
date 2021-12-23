import asyncio, typing
from .exceptions import CatchException, RedisException

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
        
    async def _execute_command(self, command: str):
        data_ = command+"\r\n"
        self.writer.write(data_.encode())
        await self.writer.drain()
        data = await self.reader.read(100)
        res = Result(data.decode('utf-8'))
        res = res.result
        res = res.replace("\r", "")
        res = res.replace("\n", "")
        catching = CatchException(text=res)
        await catching.catch_error()
        return res
        
    async def do_query(self, protocol : typing.Union[Get, Set, BasicProtocol]):
        command = getattr(protocol, 'command', None)
        
        if not command:
            raise Exception('protocol.command is not present')
            
        return await self._execute_command(command + ' ' + protocol.query)
    
