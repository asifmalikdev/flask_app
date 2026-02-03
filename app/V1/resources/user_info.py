from flask_restx import Namespace, Resource, marshal_with
from ...models import User, UserBooks
from ...extentions import db
from ..models.user_schema import (
    UserRequestSchema, UserResponseSchema, 
    UserBooksRequestSchema, UserBooksResponseSchema,
    UserBooksUpdateModel, UserUpdateSchema,
    UserBookReturnModel
)
from ...redis_app.utils import set_json, get_json  # Redis JSON helpers

user_ns = Namespace("user", description="User endpoints")


@user_ns.route("/info")
@user_ns.route("/info/<int:user_id>")
class UserInfoResource(Resource):

    @marshal_with(UserResponseSchema)
    def get(self, user_id=None):
        if user_id:
            user = User.query.get(user_id)
            if not user:
                return {"Error":"User not found"}
            return user
        users = User.query.all()
        return users, 200

    @user_ns.expect(UserRequestSchema)
    @marshal_with(UserResponseSchema)
    def post(self):
        """
        Create a new user. Clears the cache so that GET returns fresh data.
        """
        data = user_ns.payload
        name = data.get("name", "")
        email = data.get("email", "")
        data = {
        "name" : name,
        "email" : email
        }
        new_user = User(**data)
        db.session.add(new_user)

        try:
            db.session.commit()
            return new_user, 201
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 400

    @user_ns.expect(UserUpdateSchema)
    @marshal_with(UserResponseSchema)
    def patch(self):
        data = user_ns.payload
        id = data.get("id","")
        if id:
            user = User.query.get(id)
            if user:
                user.name = data.get("name", user.title)
                user.email = data.get("email", user.email)
            else:
                user = {
                    "name":data.get("name",""),
                    "email":data.get("email","")
                }

            new_user = User(**user)
            db.session.add(new_user)
            try:
                db.session.commit()
                return new_user, 201
            except Exception as e:
                db.session.rollback()
                return {"error": str(e)}, 400
        return {"message":"Id not give"}, 404


@user_ns.route("/userbooks")
class UserBooksView(Resource):
    @marshal_with(UserBooksResponseSchema)
    def get(self):
        data = UserBooks.query.all()
        return data

    @user_ns.expect(UserBooksRequestSchema)
    @marshal_with(UserBooksResponseSchema)
    def post(self):
        data = user_ns.payload
        title = data.get("title", "")
        price = data.get("price", "")
        user_id = data.get("user") 
        data = {
            "title":title,
            "price": price,
            "user_id":user_id
        }
        new_book = UserBooks(**data)
        db.session.add(new_book)
        try:
            db.session.commit()
            return new_book, 201
        except Exception as e:
            db.session.rollback()
            return {"error":str(e)}, 400
    
    @user_ns.expect(UserBooksUpdateModel)
    @marshal_with(UserBooksResponseSchema)
    def patch(self):
        data = user_ns.payload
        id = data.get("id")
        if id:
            book = UserBooks.query.get(id)
            if book:
                book.title = data.get("title", book.title)
                book.price = data.get("price", book.price)
                book.user_id = data.get("user_id", book.user_id)
            
            else:
                book = {

                    "title":data.get("title",""),
                    "price": data.get("price", ""),
                    "user_id":data.get("user_id")
                }
                new_book = UserBooks(**book)
                db.session.add(new_book)

                try:
                    db.session.commit()
                    return new_book, 201
                except Exception as e:
                    db.session.rollback()
                    return {"error": str(e)}, 400
        return data

@user_ns.route("/books_of_user/<int:user_id>")
class UserBooks(Resource):
    @marshal_with(UserBookReturnModel)
    def get(self, user_id):
        
            
        

        return "hello asif"

