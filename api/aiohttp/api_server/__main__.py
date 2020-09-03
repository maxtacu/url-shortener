#!/usr/bin/env python3

import os
import connexion
import asyncio
from aiohttp import web

from .extensions import db_queue, db, listen_for_writes
import api_server.config as config

loop = asyncio.get_event_loop()

async def db_init(loop):
    try:
        await db.set_bind(config.DATABASE_URL)
        await db.gino.create_all()
    except:
        raise Exception


def main():
    options = {
        "swagger_ui": True
        }
    connexion_app = connexion.AioHttpApp(__name__, options=options, only_one_api=True)
    connexion_app.add_api('openapi.yaml',
                arguments={'title': 'url-shortener'},
                pythonic_params=True,
                pass_context_arg_name='request')

    
    loop.run_until_complete(db_init(loop))
    

    async def start_background_tasks(app):
        app['database_writes'] = asyncio.create_task(listen_for_writes(app))


    async def cleanup_background_tasks(app):
        app['database_writes'].cancel()
        await app['database_writes']

    connexion_app.app.on_startup.append(start_background_tasks)
    connexion_app.app.on_cleanup.append(cleanup_background_tasks)

    connexion_app.run(port=8080, debug=True)

if __name__ == '__main__':
    main()
