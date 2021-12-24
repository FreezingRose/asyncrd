<h1 align="center">
<sub>
    <img src="https://media.discordapp.net/attachments/822902690010103818/923533249425313792/unknown.png" height="36">asyncrd
</sub>
A simple asyncio Redis driver for Python.

```py
import asyncrd
# connect to redis
db = await asyncrd.connect("redis://localhost:7000")
# get stuff
data = await db.get("test")
# print result
print(data)
# close connection
await db.close()
```
