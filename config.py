# Secret key configuration

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['manuel.robalinho@gmail.com']
    POSTS_PER_PAGE = 6
    LANGUAGES = ['en', 'es', 'pt']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
	
	# Email for real scneario
	#-- for a real email using gmail ----
	#SET MAIL_SERVER=smtp.googlemail.com
	#SET MAIL_PORT=587
	#SET MAIL_USE_TLS=1
	#SET MAIL_USERNAME=<manuel.robalinho@gmail.com>
	#SET MAIL_PASSWORD=<romagma20201>