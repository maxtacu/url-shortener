import connexion
import datetime

import asyncio

from api_server.config import HOSTNAME
from api_server.__main__ import db
from api_server.models.url import Url, UrlSchema

loop = asyncio.get_event_loop()

async def add_to_database(link):
    db.session.add(link)
    db.session.commit()

def create_shorturl(url=None): 
    if url is None:
        return f'Missing url parameter', 400
    else:
        existing_link = Url.query.filter(Url.original_url == url).one_or_none()
        # Create a link instance using the schema and the passed in URL
        schema = UrlSchema(exclude=("id",))
        # Do we already have this link?
        if existing_link is None:
            link = Url(original_url=url)
            loop.run_until_complete(add_to_database(link))

            link.redirect_url = HOSTNAME + link.redirect_url

            # Serialize and return the newly created link in the response
            data = schema.dump(link)

            return data, 201
        else:
            existing_link.redirect_url = HOSTNAME + existing_link.redirect_url
            data = schema.dump(existing_link)
            return data, 409


def get_stats_all(): 

    # all_records = db.session.query(Url).all()
    all_records = Url.query.all()
    for link in all_records:
        link.redirect_url = HOSTNAME + link.redirect_url
    url_schema = UrlSchema(many=True)

    return url_schema.dump(all_records)


def get_stats_shorturl(shorturl): 

    # all_records = db.session.query(Url).all()
    link_stats = Url.query.filter(Url.redirect_url == shorturl).first_or_404()
    schema = UrlSchema(exclude=("id",))

    return schema.dump(link_stats)


def redirect_shorturl(shorturl): 

    expiration = datetime.datetime.now() + datetime.timedelta(days=1)
    link = Url.query.filter(Url.redirect_url == shorturl).first_or_404()
    link.visits = link.visits + 1
    db.session.commit()
    headers = {
        'location': link.original_url,
        'expires' : expiration.strftime('%a, %d %b %Y %H:%M:%S GMT')
    }
    
    return 'Moved Permanently', 301, headers

