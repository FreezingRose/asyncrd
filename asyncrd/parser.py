import aioconsole, io, re

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

PROTOCOL = "\r\n"

class Parser():
    @classmethod
    async def encode(cls, command, query):
        res = f"*2{PROTOCOL}$4{PROTOCOL}{command}{PROTOCOL}$4{PROTOCOL}{query}{PROTOCOL}".encode()
        return res
    
    @classmethod
    async def decode(cls, text):
        text = text.decode("utf-8")
        prot = 0
        # thanks for the code Rose on discord!
        if prot == 0:
            regex = "(\${1}[0-9])"
            found = re.findall(regex, text)
            if found:
                text = text.strip(found[0])
            return text
        elif prot == -1:
            raise RedisException("{0} was not present in the result.".format(PROTOCOL))
