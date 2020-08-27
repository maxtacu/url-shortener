#!/usr/bin/env python3
from flask_sqlalchemy import SQLAlchemy 
import connexion
from sqlalchemy.exc import SQLAlchemyError
from .extensions import db, ma
from flask import render_template

import os


def main():
    connexion_app = connexion.App(__name__)

    connexion_app.app.config.from_pyfile('./config.py')

    # if os.path.exists('./api_server/shortener.db'):
    #     os.remove('./api_server/shortener.db')
    
    connexion_app.add_api('./openapi.yaml', pythonic_params=True)

    try:
        db.init_app(connexion_app.app)
        ma.init_app(connexion_app.app)
    except SQLAlchemyError as e:
        print(e)
    
    with connexion_app.app.app_context():
        db.create_all()

    @connexion_app.app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()


    connexion_app.run(port=8080)
    # print(connexion_app.host)
    

if __name__ == '__main__':
    main()
