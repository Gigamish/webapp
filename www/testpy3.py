import sys
import orm,asyncio
from models import User,Blog,Comment

@asyncio.coroutine
def test( loop ):
    yield from orm.create_pool( loop = loop, user='root', password='password', db='webapp' )
    u=User(name='test22',email='test22@test.com',passwd='test',image='about:blank')
    yield from u.save()
    yield from orm.destroy_pool()
if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))    
#loop.run_until_complete( asyncio.wait([test( loop )]) )  
    loop.close()
    if loop.is_closed():
        sys.exit(0)
