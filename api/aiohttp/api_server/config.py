import os 

DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://postgres:password@localhost:5432/urlshortener')

HOSTNAME = os.environ.get('SHORT_HOSTNAME', 'https://aiohttp.shortdemo.tk/')
