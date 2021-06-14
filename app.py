
from security import authenticate, identity
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
import datetime
from resources.user import UserRegister
from resources.items import Item,Itemlist
from db import db
import os
import sqlite3

app=Flask(__name__)
app.secret_key="shivam"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL1', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api=Api(app)
jwt=JWT(app,authenticate,identity) #/auth

app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=1000)
#for jwt token expire time can use day ex.  (days=10)

items =[{'name':'urdu'},{'name':'urdu'},{'name':'hindi'}]

api.add_resource(Item,'/<string:name>')
api.add_resource(Itemlist,'/')
api.add_resource(UserRegister,'/Register')


db.init_app(app)

