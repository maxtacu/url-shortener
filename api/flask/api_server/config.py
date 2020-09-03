import os 

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://root:password@localhost:3306/flaskshortener')
SQLALCHEMY_TRACK_MODIFICATIONS = False

HOSTNAME = 'https://flask.shortdemo.tk/'
SECRET_KEY = os.urandom(16)