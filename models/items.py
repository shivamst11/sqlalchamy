
from db import db

class ItemModel(db.Model):

    __tablename__="items"
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80))

    def __init__(self,name):
        self.name =name;

    def json(self):
        return {'name':self.name}


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()




    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def item(cls, name):
        return cls.query.filter_by(name=name).first()








