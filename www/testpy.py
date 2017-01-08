import asyncio,sys
import orm
from models import User, Blog, Comment
if __name__=="__main__":
    loop = asyncio.get_event_loop()
    @asyncio.coroutine
    def test():

        yield from orm.create_pool(loop=loop,host='localhost', port=3306, user='root', password='password', db='webapp')
        u = User(name='sly', email='slysly759@gmail.com', password='1234567890', image='about:blank',admin_flag=True)

        yield from u.save()
        yield from orm.destroy_pool()
    
    loop.run_until_complete(test(loop))
    __pool.close()
    loop.run_until_complete(test())
    loop.close()
    if loop.is_closed():
        sys.exit(0)
