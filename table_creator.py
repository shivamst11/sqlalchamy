from db import db
from app import app

with app.app_context():
    # your code here
    db.create_all()


