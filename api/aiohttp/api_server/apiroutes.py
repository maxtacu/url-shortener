import datetime
from aiohttp import web

from api_server.models.url import Url, UrlSchema
from api_server.config import HOSTNAME
from api_server.extensions import db_queue
import json


async def create_shorturl(request: web.Request, url=None) -> web.Response:

    # if request.has_body:
    #     url = request.['url']
    url = request.query['url']
    if url is None:
        return f'Missing url parameter', 400
    else:
        existing_link = await Url.query.where(Url.original_url == url).gino.first()

        schema = UrlSchema(exclude=("id",))
        # Do we already have this link?
        if existing_link is None:
            newUrl = Url(original_url=url)
            await db_queue.put(newUrl)

            # Serialize Url object into json
            result = schema.dump(newUrl)            
            return web.json_response(result, status=201)
    
        else:
            response = schema.dump(existing_link)

            return web.json_response(response, status=409)


async def get_stats_all(request: web.Request, ) -> web.Response:

    all_records = await Url.query.gino.all()
    url_schema = UrlSchema(many=True)
    return web.json_response(url_schema.dump(all_records), status=200)


async def get_stats_shorturl(request: web.Request, shorturl) -> web.Response:
    
    link_stats = await Url.query.where(Url.redirect_url == shorturl).gino.first()
    schema = UrlSchema(exclude=("id",))
    return web.json_response(schema.dump(link_stats), status=200)


async def redirect_shorturl(request: web.Request, shorturl) -> web.Response:

    expiration = datetime.datetime.now() + datetime.timedelta(days=1)
    link = await Url.query.where(Url.redirect_url == shorturl).gino.first()
    # link.visits = link.visits + 1
    await link.update(visits=link.visits + 1).apply()
    headers = {
        'location': link.original_url,
        'expires' : expiration.strftime('%a, %d %b %Y %H:%M:%S GMT')
    }
    
    return web.Response(status=301, headers=headers)
