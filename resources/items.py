

from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from flask import jsonify
from models.items import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()


    parser.add_argument('name',
                        type=str,
                        required=False,
                        help=" this field cannot be left blank"
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=False,
                        help=" Every item needs a store id."
                        )
    
    @jwt_required()
    def get(self,name):
        item=ItemModel.item(name)

        if item:
            return item.json(),200 if item else 404
        
    @jwt_required()
    def post(self,name):
        data=Item.parser.parse_args()
        item = ItemModel.item(data['name'])
        item1=ItemModel(data["name"],data['store_id'])
        if item:
            return {"msg":"Item is already exists"},400
        try:
            item1.save_to_db()
        except:
            return {"msg": "An error occurred inserting the item."},500

        return item1.json(), 201





    def delete(self,name):

        item1 = ItemModel.item(name)
        if item1:
            item1.delete_from_db()

        return {'message': 'Item deleted'}

    def put(self,name):
        data = Item.parser.parse_args()
        item = ItemModel.item(data['name'])

        if item:
            item.name=data["name"]
        else:
            item=ItemModel(**data)

        item.save_to_db()

        return item.json(),202







class Itemlist(Resource):
    def get(self):
        data=ItemModel.query.all()
        item=[]
        for x in data:
            data=x.json()
            item.append(data)
        return {"item":item}

