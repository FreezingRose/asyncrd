import aioconsole
from .exceptions import RedisException, RedisCommandUnknown, RedisWrongType

PROTOCOL = "\r\n"

*2\r\n$4\r\nLLEN\r\n$6\r\nmylist\r\n

class Parser():
    async def encode(self, command, query):
        res = ""
        res += f"*2{PROTOCOL}$4{PROTOCOL}{command}{PROTOCOL}$6{PROTOCOL}{query}{PROTOCOL}"
        return res.encode()
    
    async def decode(self, text : str):
        prot = text.find(PROTOCOL)
        if prot == 0:
            protocol_list = ['$', "-", "+"]
            if text[0] not in protocol_list:
                raise RedisException("These ({0}) were not present in the result.".format(", ".join(protocol_list)))
                return
            if "-1" in text:
                protocol_list = ['$', '+']
            for i in protocol_list:
                text = text.strip(i)
            text = text.strip(PROTOCOL)
            results = ["ERR ", "WRONGTYPE ", "OK", "-1"]
            if text.startswith(results[0]):
                text = text.strip(results[0])
                if "unknown" in command:
                    raise RedisCommandUnknown(text)
            if text.startswith(results[1]):
                res = results[1]
                text = text.strip(res)
                raise RedisWrongType(text)
             if text.startswith(results[2]):
                res = results[2]
                text = text.strip(res)
                return "OK"
            if text.startswith(results[3]):
                res = results[3]
                text = text.strip(res)
                return "NONE"
        elif prot == -1:
            raise RedisException("{0} was not present in the result.".format(PROTOCOL))
