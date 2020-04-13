#-----------------------------------------------------------
# Conection test
'''  Comentado
# SELECT Operation
# https://www.tutorialspoint.com/sqlite/sqlite_python.htm
import sqlite3

conn = sqlite3.connect('app.db')
print("Opened database successfully");

cursor = conn.execute("SELECT id, username, email from USERS")
for row in cursor:
   print("ID = ", row[0])
   print("USERNAME = ", row[1])
   print("EMAIL = ", row[2], "\n")

print("Operation done successfully");
conn.close()
'''
#------------------------------------------------------
def open_db():
   print('DB app opened...')
   from app import db
   from app.models import User, Post
   return db, User, Post

def close_db():
   db.session.commit()
   print('DB app closed...')
   return
#-----------------------------------------------------
# Conection test to APP microblog - Add user
'''
from app import db
from app.models import User, Post

t_user = 'Manuel Robalinho'
t_email = 'manuel.robalinho@gmail.com'
print('Inserindo registo de users ...', t_user)
u = User(username=t_user, email=t_email)
db.session.add(u)
db.session.commit()
print('Registo inserido:',t_user)
'''
#--------------------------------------------------
# List users from data base
'''
from app import db
from app.models import User, Post

users = User.query.all()
users
for u in users:
    print('User:', u.id, u.username)
    '''
#----------------------------------------------
# Test to get one user
'''
from app import db
from app.models import User, Post

u = User.query.get(1)
print(u)
'''
#--------------------------------------------
# Test to blog post
'''
db, User, Post=open_db()
print('Insert a post ...')
u = User.query.get(3)
p = Post(body='my 3 post test by Manuel Robalinho!', author=u)
db.session.add(p)
print('Appended post:',u)
close_db()
'''
#----------------------------------------------
# get all posts written by a user
'''
db, User, Post=open_db()
print('Get all post ...')
u = User.query.get(3)
allp=u.posts.all()
print(allp)
#---
# print post author and body for all posts
print('---- Print all posts ----')
posts = Post.query.all()
for p in posts:
    print(p.id, p.author.username, p.body)
    '''
#-------------------------------------------
# get all users in reverse alphabetical order
'''
print('---- all users in reverse alphabetical order ----')
db, User, Post=open_db()
x_u = User.query.order_by(User.username.desc()).all()
print('ID User         Email')
for u in x_u:
    print(u.id, u.username, u.email)
    '''
#-------------------------------------------
#  Delete USERS and POSTS
'''
print('Delete Users and Posts from APP data base ....')
db, User, Post=open_db()
users = User.query.all()
for u in users:
    db.session.delete(u)
#---
posts = Post.query.all()
for p in posts:
    db.session.delete(p)
db.session.commit()
'''
#--------------------------------------
# HASH
'''
from werkzeug.security import generate_password_hash, check_password_hash

# passw  = correct password
passw   = 'foobar'

# passw_f = false password
passw_f = 'xpto'
hash = generate_password_hash(passw)
print('Password:', passw, ', Encrypted', hash)

x_tf = check_password_hash(hash, passw)
print('Password:', passw_f, '  is:', x_tf)
'''
#---------------------------------------
# Test Password with HASH
'''
print('Testing HASH password ....')
db, User, Post=open_db()
u = User(username='susan', email='susan@example.com')
u.set_password('mypassword')
x_tf = u.check_password('anotherpassword')
print(x_tf)
x_tf = u.check_password('mypassword')
print(x_tf)
'''
#---------------------------------------
#  Create AVATAR
'''
from hashlib import md5
x_y = 'https://www.gravatar.com/avatar/' + md5(b'manuel.robalinho@gmail.com').hexdigest()
print(x_y)
'''
#----------------------------------------------
# Send Email
# https://stackabuse.com/how-to-send-emails-with-gmail-using-python/
# Tested OK
'''
import smtplib

gmail_user = 'manuel.robalinho@gmail.com'
gmail_password = 'fxsaglakxrxztqfc'
# a password é obtiga na configuração de segurança em 2 passos do google
# ao definir password para acesso de APPs
# https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python/27515833#27515833

#-- create email
sent_from = gmail_user
to = ['manuel.robalinho@hotmail.com', 'robalinho.manuel@gmail.com']
subject = 'OMG Super Important Message - Teste Python'
body = 'Hey, whats up?\n\n- You. I am testink Python sending email'

email_text = """
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

print(email_text)
#   - send email
try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:
    print('Something went wrong...')
'''
#------------------------------------------
#   SEND Email
# https://docs.python.org/3.5/library/smtplib.html
# https://docs.python.org/3.5/library/email-examples.html#email-examples
'''
import smtplib

def prompt(prompt):
    return input(prompt).strip()

fromaddr = prompt("From: ")
toaddrs  = prompt("To: ").split()
print("Enter message, end with ^D (Unix) or ^Z (Windows):")

# Add the From: and To: headers at the start!
msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs)))
while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    msg = msg + line

print("Message length is", len(msg))

server = smtplib.SMTP('localhost')
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

'''
#-------------------------------------
#  SEND email
# https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python/27515833#27515833
# Tested OK
'''
import smtplib
fromaddr = 'manuel.robalinho@gmail.com'
toaddrs  = 'robalinho.manuel@gmail.com'
msg = "\r\n".join([
  "From: manuel.robalinho@gmail.com",
  "To: robalinho.manuel@gmail.com",
  "Subject: Just a message to teste",
  "",
  "Why, oh why"
  ])
username = 'manuel.robalinho@gmail.com'
# a password é obtiga na configuração de segurança em 2 passos do google
# ao definir password para acesso de APPs
password = 'fxsaglakxrxztqfc'
#....
server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.ehlo()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.close()
print('successfully sent the mail')

'''
#-------------------------------------
#  SEND email
'''
db, User, Post = open_db()

from flask_mail import Message
from app import mail

msg = Message('test subject', sender=app.config['ADMINS'][0], recipients=['your-email@example.com'])
msg.body = 'text body'
msg.html = '<h1>HTML body</h1>'
mail.send(msg)
'''
#-------------------------------
#   JSON Web Token
# The {'a': 'b'} dictionary is an example payload that is going to be written
# into the token. To make the token secure, a secret key needs to be provided
# to be used in creating a cryptographic signature.
# For this example I have used the string 'my-secret', but with the application
# I'm going to use the SECRET_KEY from the configuration. The algorithm argument
# specifies how the token is to be generated. The HS256 algorithm is the most
# widely used.
'''
import jwt
token = jwt.encode({'a': 'b'}, 'my-secret', algorithm='HS256')
print('Token:', token)
xy = jwt.decode(token, 'my-secret', algorithms=['HS256'])
print(xy)
'''
#----------------
# Test Timezone 
from datetime import datetime
print('Time now:', str(datetime.now()))
print('Time UTC now:',str(datetime.utcnow()))
#--------------------------------
#  Using Flask Moment
'''
from flask_moment import Moment
moment = Moment()

def create_app(config):
   app = Flask(name)
   app.config.from_object(config)
# initialize moment on the app within create_app()
   moment.init_app(app)

app = create_app(prod_config)
   
moment = Moment(app)
t = moment('2017-09-28T21:45:23Z')

print(t)
'''
#------------------------
# Translate
# Testado OK. A MS_TRANSLATOR_KEY foi
# gerado no AZURE na API translator com o user manuel.robalinho@hotmail.com

import json
import requests
from flask_babel import _

MS_TRANSLATOR_KEY = '8fbc6240736c4ba7ad210bf8adcca198'

def translate(text, source_language, dest_language):

    auth = {'Ocp-Apim-Subscription-Key': MS_TRANSLATOR_KEY}
    r = requests.get('https://api.microsofttranslator.com/v2/Ajax.svc'
                     '/Translate?text={}&from={}&to={}'.format(
                         text, source_language, dest_language),
                     headers=auth)
    if r.status_code != 200:
           return _('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8-sig'))
   
t = translate('Hi, how are you today?', 'en', 'pt')  # English to Spanish
print('Translate:',t)


