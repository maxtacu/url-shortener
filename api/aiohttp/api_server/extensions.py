import sqlalchemy as sa
from marshmallow import Schema
import asyncio
from aiomysql.sa import create_engine

metadata = sa.MetaData()

# Initialize Marshmallow
schema = Schema()

# Initialize Queue
db_queue = asyncio.Queue()


