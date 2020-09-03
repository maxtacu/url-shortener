import datetime
from aiohttp import web

from api_server.models.url import Url, UrlSchema
from api_server.extensions import queue


async def create_shorturl(request: web.Request, url=None) -> web.Response:
    """Add URL

    Create your short link

    :param url: 
    :type url: str

    """
    print(1)
    return web.json_response(data, status=200)


async def get_stats_all(request: web.Request, ) -> web.Response:
    """All URL-shortener stats

    Get stats on all existing links in database

    """
    print(1)
    await queue.put(1)
    return web.json_response(data, status=200)


async def get_stats_shorturl(request: web.Request, shorturl) -> web.Response:
    """Stats for a specific url

    Get specific link stats

    :param shorturl: 
    :type shorturl: str

    """
    return web.json_response(data, status=200)


async def redirect_shorturl(request: web.Request, shorturl) -> web.Response:
    """Redirect URL

    Redirect to the long url which was added

    :param shorturl: 
    :type shorturl: str

    """
    headers = {
        'location': link.original_url,
        'expires' : expiration.strftime('%a, %d %b %Y %H:%M:%S GMT')
    }
    return web.Response(status=301, headers=headers)
