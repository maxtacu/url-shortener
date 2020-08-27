import os 

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///shortener.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

HOSTNAME = 'http://localhost:8080/'
SECRET_KEY = os.urandom(16)