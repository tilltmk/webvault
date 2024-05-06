import os
import secrets

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', default=secrets.token_hex(32))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///webvault.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ARCHIVE_FOLDER = 'archived_websites'