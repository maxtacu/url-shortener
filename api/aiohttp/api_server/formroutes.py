# import connexion
import datetime

import asyncio

from api_server.config import HOSTNAME
from api_server.extensions import db
from api_server.models.url import Url, UrlSchema
from flask import Blueprint, render_template, request
from .util import add_link

htmlresponse = Blueprint('htmlresponse', __name__)


@htmlresponse.route('/')
def index():
    return render_template('index.html') 
    pass


@htmlresponse.route('/add', methods=['POST'])
def create_shorturl(): 
    original_url = request.form['original_url']
    if original_url is None:
        return f'Missing url', 400
    else:   
        existing_link = Url.query.filter(Url.original_url == original_url).one_or_none()
        # Create a link instance using the schema and the passed in URL
        schema = UrlSchema(exclude=("id",))
        # Do we already have this link?
        if existing_link is None:
            response = add_link(original_url, schema)
    
            return render_template('link_added.html', 
                redirect_url=response['redirect_url'], original_url=response['original_url']), 201
        else:
            existing_link.redirect_url = HOSTNAME + existing_link.redirect_url
            response = schema.dump(existing_link)

            return render_template('link_added.html', 
                redirect_url=response['redirect_url'], original_url=response['original_url']), 409


# def get_stats_all(): 

#     # all_records = db.session.query(Url).all()
#     all_records = Url.query.all()
#     for link in all_records:
#         link.redirect_url = HOSTNAME + link.redirect_url
#     url_schema = UrlSchema(many=True)

#     return url_schema.dump(all_records)

@htmlresponse.route('/stats')
def stats():
    all_records = Url.query.all()
    for link in all_records:
        link.redirect_url = HOSTNAME + link.redirect_url

    return render_template('stats.html', links=all_records)


# def get_stats_shorturl(shorturl): 

#     # all_records = db.session.query(Url).all()
#     link_stats = Url.query.filter(Url.redirect_url == shorturl).first_or_404()
#     schema = UrlSchema(exclude=("id",))

#     return schema.dump(link_stats)


# def redirect_shorturl(shorturl): 

#     expiration = datetime.datetime.now() + datetime.timedelta(days=1)
#     link = Url.query.filter(Url.redirect_url == shorturl).first_or_404()
#     link.visits = link.visits + 1
#     db.session.commit()
#     headers = {
#         'location': link.original_url,
#         'expires' : expiration.strftime('%a, %d %b %Y %H:%M:%S GMT')
#     }
    
#     return 'Moved Permanently', 301, headers

