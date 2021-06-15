
from flask_restful import Resource,reqparse
from models.user import  UserModel








class UserRegister(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="this field cannot be empty"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="this field cannot be empty"
                        )

    def post(self):
        data=UserRegister.parser.parse_args()





        check=UserModel.find_by_username(data["username"])
        if check is None:
            user1=UserModel(data["username"],data["password"])
            user1.save_to_db()
            return {"msg":'item is created'},201
        else:
            return {'msg':'username is already exists'},400






        

