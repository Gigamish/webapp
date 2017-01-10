import asyncio,sys
import aiomysql
import orm
from models import User, Blog, Comment

loop = asyncio.get_event_loop()


@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop=loop,host = 'localhost', port=3306, user='root', password='password', db='webapp')
    u = User(name='sly', email='slysly759@gmail.com', password='1234567890', image='about:blank',admin_flag=True)
    yield from u.save()
    yield from destory_pool()

for x in test(loop):
    pass


"""
loop.run_until_complete(test())
loop.close()
"""
