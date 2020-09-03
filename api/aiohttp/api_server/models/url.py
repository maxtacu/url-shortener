from api_server.extensions import db, ma
from datetime import datetime, timedelta 

from random import choices
import string


class Url(db.Model):
    __tablename__ = 'url_list'
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    redirect_url = db.Column(db.String(7), unique=True)
    expires = db.Column(db.DateTime)
    visits = db.Column(db.Integer, default=0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.redirect_url = self.generate_redirect_url()
        self.expires = datetime.now() + timedelta(days=1)

    
    def generate_redirect_url(self):
        characters = string.digits + string.ascii_letters # numbers + lower and upercase letters
        short_url = ''.join(choices(characters, k=7))

        link = self.query.filter_by(redirect_url=short_url).first()

        if link:
            return self.generate_redirect_url()
                
        return short_url


class UrlSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Url
        sqla_session = db.session  

