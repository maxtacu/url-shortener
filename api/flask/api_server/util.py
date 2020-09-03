import asyncio

from api_server.extensions import db
from api_server.models.url import Url
from api_server.config import HOSTNAME

loop = asyncio.get_event_loop()

def add_link(new_link, schema):
    
    async def write_to_database(link):
        db.session.add(link)
        db.session.commit()

    link = Url(original_url=new_link)
    loop.run_until_complete(write_to_database(link))

    link.redirect_url = HOSTNAME + link.redirect_url

    # Serialize and return the newly created link in the response
    data = schema.dump(link)

    return data