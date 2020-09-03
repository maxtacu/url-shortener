from datetime import datetime, timedelta 
from api_server.extensions import db
from api_server.__main__ import loop
from marshmallow import Schema, fields
from api_server.config import HOSTNAME

from random import choices
import string
import asyncio
import nest_asyncio

nest_asyncio.apply()


class Url(db.Model):
    __tablename__ = 'url_list'
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    redirect_url = db.Column(db.String(7), unique=True)
    expires = db.Column(db.DateTime)
    visits = db.Column(db.Integer, default=0)

    def __init__(self,  **kwargs):
        super().__init__(**kwargs)
        self.redirect_url = loop.run_until_complete(self.generate_redirect_url())
        self.expires = datetime.now() + timedelta(days=3)

    
    async def generate_redirect_url(self):
        characters = string.digits + string.ascii_letters # numbers + lower and upercase letters
        short_url = ''.join(choices(characters, k=7))

        link = await self.query.where(self.redirect_url==short_url).gino.first()

        if link:
            return await self.generate_redirect_url()
                
        return short_url


class UrlSchema(Schema):
    id = fields.Int()
    original_url = fields.Str()
    redirect_url = fields.Function(lambda obj: HOSTNAME + obj.redirect_url)
    expires = fields.DateTime()
    visits = fields.Int(default=0)
