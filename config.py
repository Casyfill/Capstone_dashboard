# it activates the cross-site request forgery prevention (note that this setting is enabled by default in current versions of Flask-WTF). In most cases you want to have this option enabled as it makes your app more secure
WTF_CSRF_ENABLED = True

# this is only needed when CSRF is enabled, and is used to create a cryptographic token that is used to validate a form. When you write your own apps make sure to set the secret key to something that is difficult to guess.
# SECRET_KEY = 'you-will-never-guess'


CRIME_RECORDS = [
        {
            'crimeId':'12',
            'modeOfEntry': 'Front Door'
        },
        {
            'crimeId':'43',
            'modeOfEntry': 'Side Window'
        },
        {
            'crimeId':'78',
            'modeOfEntry': 'Back Door'
        },
        {
            'crimeId':'54',
            'modeOfEntry': 'Front Door'
        }
    ]
    
    
    
# setting up database
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True