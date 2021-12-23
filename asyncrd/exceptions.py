import asyncio, typing
import aioconsole
from .parser import Parser

class RedisOK():
    def __init__(self, message : str):
        self.msg = message
        
class BaseRedisException(Exception):
    pass

class RedisException(BaseRedisException):
    def __init__(self, message : str):
        super().__init__(message)
        
class RedisCommandUnknown(BaseRedisException):
    def __init__(self, message : str):
        super().__init__(message)
        
class RedisWrongType(BaseRedisException):
    def __init__(self, message : str):
        super().__init__(message)


class CatchException():
    def __init__(self, text : str):
        self.text = text
        
    async def catch_error(self):
        parser = Parser()
        res = await parser.decode(self.text)
        res[0] = ""
        res[1] = ""
        return res
            
        
