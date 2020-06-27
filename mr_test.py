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
'''
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
'''
#----------------------------
#   Elasticsearch
# https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html
# https://www.elastic.co/guide/en/elastic-stack-get-started/current/get-started-elastic-stack.html
#
'''
import os
import pprint 
from elasticsearch import Elasticsearch
pp = pprint.PrettyPrinter(indent=4)

print(os.getcwd())
es = Elasticsearch('http://localhost:9200')
print('')
print('---- Insert record -----------: this is a test')
ih = es.index(index='my_index', id=1, body={'text': 'this is a test'})
pp.pprint(ih)

print('')
print('---- Insert record -----------: second')
ih = es.index(index='my_index', id=2, body={'text': 'a second test'})
pp.pprint(ih)

print('')
print('---- Insert record -----------: teste do robalinho')
ih = es.index(index='my_index', id=2, body={'text': 'teste do robalinho'})
pp.pprint(ih)

print('')
print('---- Insert record -----------: mais um robalinho a fazer test')
ih = es.index(index='my_index', id=2, body={'text': 'mais um robalinho a fazer test'})
pp.pprint(ih)

print('')
print('---- 1 Search record -----------: this test')
sh = es.search(index='my_index', body={'query': {'match': {'text': 'this test'}}})
pp.pprint(sh)

print('')
print('---- 2 Search record -----------: second')
sh = es.search(index='my_index', body={'query': {'match': {'text': 'second'}}})
pp.pprint(sh)

print('')
print('---- 3 Search record -----------: robalinho')
sh = es.search(index='my_index', body={'query': {'match': {'text': 'robalinho'}}})
pp.pprint(sh)

# delete my_index
es.indices.delete('my_index')
'''
#----------------------------------
# Test Elasticsearch is running
# make sure ES is up and running
# https://github.com/ernestorx/es-swapi-test/blob/master/ES%20notebook.ipynb
# https://towardsdatascience.com/getting-started-with-elasticsearch-in-python-c3598e718380
'''
import pprint 
import requests
pp = pprint.PrettyPrinter(indent=1)

res = requests.get('http://localhost:9200')
pp.pprint(res.content)

# --- connect
# connect to our cluster
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
print(es)


#index some test data
doc = {
    'author': 'paulo',
    'text': 'Elasticsearch: one, two , three , four, five six',
    'timestamp': datetime.now(),
}

xid = 11
res = es.index(index='test-index', id=xid, body=doc)
print('---')
print('Inserido Registo:', xid, res['result'])
doc = {
    'author': 'manuel',
    'text': 'Elasticsearch: ten, one, five',
    'timestamp': datetime.now(),
}

xid = 12
res = es.index(index='test-index', id=xid, body=doc)
print('---')
print('Inserido Registo:', xid, res['result'])

#let's iterate people documents and index them
doc = {
"name": "Luke Skywalker",
	"height": "172",
	"mass": "77",
	"hair_color": "blond",
	"birth_year": "19BBY",
	"gender": "male",
}
xid = 11
res = es.index(index='test-index2', doc_type='people', id=xid, body=doc)
print('---')
print('Inserido Registo:', xid, res['result'])

doc = {
"name": "Luke Robalinho",
	"height": "172",
	"mass": "77",
	"hair_color": "blond",
	"birth_year": "19BBY",
	"gender": "male",
}
xid = 12
res = es.index(index='test-index2', doc_type='people', id=xid, body=doc)
print('---')
print('Inserido Registo:', xid, res['result'])

print('-- Read all records : test-index-')
res = es.search(index="test-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total']['value'])
for record in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % record["_source"])

print('-- Read all records : test-index2 -')
res = es.search(index="test-index2", body={"query": {"match_all": {}}})
print("Got %d record:" % res['hits']['total']['value'])
for record in res['hits']['hits']:
    print("%(name)s %(gender)s: %(birth_year)s %(hair_color)s" % record["_source"])

#  search query:
xname = 'one'
print('-- Search for: ', xname)
res = es.search(index="test-index", body={"query": {"match": {'text':xname}}})
print("Got %d Hits:" % res['hits']['total']['value'])
for record in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % record["_source"])

xname = 'Luke'
print('-- Search for: ', xname)
res = es.search(index="test-index2", body={"query": {"match": {'name':xname}}})
print("Got %d Hits:" % res['hits']['total']['value'])
for record in res['hits']['hits']:
    print("%(name)s %(gender)s: %(birth_year)s %(hair_color)s" % record["_source"])
'''    
#--------------------------------------
# Test Post shearch - Elasticsearch
# https://tryolabs.com/blog/2015/02/17/python-elasticsearch-first-steps/
# https://elasticsearch-py.readthedocs.io/en/master/
#
'''
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

doc = {
    'author': 'manuel',
    'text': 'Elasticsearch: one, two , three , four',
    'timestamp': datetime.now(),
}
xid = 2
res = es.index(index="test-index", id=xid, body=doc)
print('---')
print('Inserido Registo:', xid, res['result'])


res = es.get(index="test-index", id=xid)
print('---')
print('Get registo:', xid, '  Source:', res['_source'])

es.indices.refresh(index="test-index")

print('---')
res = es.search(index="test-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
        
'''
#-------------------------------------
#  Using Decorator
# importing libraries
#  https://www.programiz.com/python-programming/decorator
'''
import time 
import math 
  
# decorator to calculate duration 
# taken by any function. 
def calculate_time(func): 
    print('2')  
    # added arguments inside the inner1, 
    # if function takes any arguments, 
    # can be added like this. 
    def inner1(*args, **kwargs): 
        print('3') 
        # storing time before function execution 
        begin = time.time() 
          
        func(*args, **kwargs) 
  
        # storing time after function execution 
        end = time.time() 
        print("Total time taken in : ", func.__name__, end - begin) 
  
    return inner1 
  
  
  
# this can be added to any function present, 
# in this case to calculate a factorial 
@calculate_time
def factorial(num): 
    print('1')
    # sleep 2 seconds because it takes very less time 
    # so that you can see the actual difference 
    time.sleep(2) 
    print(math.factorial(num)) 
  
# calling the function. 
factorial(10)
'''
# ---------------
# Using Decorators
# https://www.programiz.com/python-programming/decorator

def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b

xc = divide(6,3)
print('Result:', xc)








