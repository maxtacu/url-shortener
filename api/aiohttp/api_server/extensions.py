import asyncio
import asyncpg
from gino import Gino
# from api_server.models.url import Url

db = Gino()

# Initialize Queue
db_queue = asyncio.Queue()


async def listen_for_writes(app):
    while True:
        # wait for an item from the producer
        link = await db_queue.get()
        if link is None:
            print(1)
            # the producer emits None to indicate that it is done
            break
        
        # simulate i/o operation using sleep
        # await asyncio.sleep(2)
        
        # process the item
        print(f"Received new URL: {link.original_url}")

        await link.create()

        