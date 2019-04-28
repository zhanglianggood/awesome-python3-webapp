from ORM import connectPool as con
from MODEL.models import User
import asyncio


async def test(loop):
    await con.create_pool(loop=loop, user='root', password='1qazXSW@', db='test')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await u.save()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()