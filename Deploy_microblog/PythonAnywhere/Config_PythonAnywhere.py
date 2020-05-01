# Secret key configuration

import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
print('load MICROBLOG.ENV  file:' , basedir)
load_dotenv(os.path.join(basedir, 'microblog.env'))

class Config(object):
    print('Read Config ...' )
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    #--- Data Base
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username='Mrobalinho' ,
    password='normal'    ,
    hostname='localhost'  ,
    databasename='Mrobalinho$app')

    SQLALCHEMY_POOL_RECYCLE = 299
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #---
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']
    LANGUAGES = ['en', 'es', 'pt']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    POSTS_PER_PAGE = 25
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    print('----- Config --------')
    print('SECRET_KEY :', SECRET_KEY)
    print('SQLALCHEMY_DATABASE_URI :', SQLALCHEMY_DATABASE_URI)
    print('SQLALCHEMY_TRACK_MODIFICATIONS :', SQLALCHEMY_TRACK_MODIFICATIONS)
    print('MAIL_SERVER :', MAIL_SERVER)
    print('MAIL_PORT :', MAIL_PORT)
    print('MAIL_USE_TLS  :', MAIL_USE_TLS)
    print('MAIL_USERNAME :', MAIL_USERNAME)
    print('MAIL_PASSWORD :', MAIL_PASSWORD)
    print('ADMINS :', ADMINS)
    print('LANGUAGES :', LANGUAGES)
    print('MS_TRANSLATOR_KEY :', MS_TRANSLATOR_KEY)
    print('ELASTICSEARCH_URL :', ELASTICSEARCH_URL)
    print('POSTS_PER_PAGE :', POSTS_PER_PAGE)
    print('LOG_TO_STDOUT :', LOG_TO_STDOUT)
    print('----Finish load Config --------')
	# Email for real scneario
	#-- for a real email using gmail ----
	#SET MAIL_SERVER=smtp.googlemail.com
	#SET MAIL_PORT=587
	#SET MAIL_USE_TLS=1
	#SET MAIL_USERNAME=<manuel.robalinho@gmail.com>
	#SET MAIL_PASSWORD=<romagma20201>
