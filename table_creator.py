from db import db
from app import app

with app.app_context():
    db.init_app(app)
    # your code here
    db.create_all()


