import asyncio, typing
import aioconsole

class RedisOK():
    def __init__(self, message : str):
        self.msg = message

class RedisException(Exception):
    def __init__(self, message : str):
        super().__init__(message)
        
class RedisCommandUnknown(Exception):
    def __init__(self, message : str):
        super().__init__(message)
        
class RedisWrongType(Exception):
    def __init__(self, message : str):
        super().__init__(message)


class CatchException():
    def __init__(self, text : str):
        self.text = text
        
    async def catch_error(self):
        if self.text.startswith("-ERR") or self.text.starswith("-WRONGTYPE "):
            text = self.text.split("-ERR ")
            if "unknown" in text[1]:
                text_one = text[1]
                raise RedisCommandUnknown(text_one)
                return
            if "Operation against a key holding the wrong kind of value" in text[1]:
                text_one = text[1]
                raise RedisWrongType(text_one)
                return               
            raise RedisException(text[1])
            return
        if self.text.startswith("+OK"):
            res = RedisOK("OK")
            return res.msg
        return self.text
            
        
