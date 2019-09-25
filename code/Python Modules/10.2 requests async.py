# https://www.youtube.com/watch?v=a6fIbtFB46g&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=102
from requests_html import HTML, HTMLSession, AsyncHTMLSession
import time

asession = AsyncHTMLSession()

t1 = time.perf_counter()


async def get_delay1():
    r = await asession.get("https://httpbin.org/delay/1")
    return r


async def get_delay2():
    r = await asession.get("https://httpbin.org/delay/2")
    return r


async def get_delay3():
    r = await asession.get("https://httpbin.org/delay/3")
    return r


results = asession.run(get_delay1, get_delay2, get_delay3)

for result in results:
    print(result.html.url)

t2 = time.perf_counter()

print(f"{t2-t1} secs")
