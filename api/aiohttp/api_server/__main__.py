#!/usr/bin/env python3

import os
import connexion
import asyncio
from aiohttp import web

from .extensions import db_queue
from sqlalchemy.exc import SQLAlchemyError


def main():
    options = {
        "swagger_ui": True
        }
    connexion_app = connexion.AioHttpApp(__name__, options=options, only_one_api=True, debug=True)
    connexion_app.add_api('openapi.yaml',
                arguments={'title': 'url-shortener'},
                pythonic_params=True,
                pass_context_arg_name='request')

    # connexion_app.app.config.from_pyfile('./config.py')
    # try:
    #     db.init_app(connexion_app.app)
    #     ma.init_app(connexion_app.app)
    # except SQLAlchemyError as e:
    #     print(e)
    
    # with connexion_app.app.app_context():
    #     db.create_all()
    
    # app = web.Application()
    
    # async def handler(request):
    #     print(1)
    #     # await spawn(request, coro(3))
    #     await queue.put(1)
    #     return web.Response()


    async def listen_for_writes(app):
        while True:
            # wait for an item from the producer
            item = await db_queue.get()
            if item is None:
                # the producer emits None to indicate that it is done
                break

            # process the item
            print('consuming item {}...'.format(item))
            # simulate i/o operation using sleep
            await asyncio.sleep(2)


    async def start_background_tasks(app):
        app['database_listener'] = asyncio.create_task(listen_for_writes(app))


    async def cleanup_background_tasks(app):
        app['database_listener'].cancel()
        await app['database_listener']

    connexion_app.app.on_startup.append(start_background_tasks)
    connexion_app.app.on_cleanup.append(cleanup_background_tasks)

    connexion_app.run(port=8080, debug=True)

if __name__ == '__main__':
    main()
