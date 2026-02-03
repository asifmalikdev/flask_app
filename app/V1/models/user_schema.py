from flask_restx import fields, Model

UserRequestSchema = Model("UserRequestSchema", {
    "name": fields.String(description="User name", example = "User1"),
    "email": fields.String(description="User email", example = "user1@gmail.com"),
})

UserUpdateSchema = Model("UserUpdateSchema",{
    "id":fields.Integer(required = True),
    "name":fields.String(required = False, description = "User Name", example = "user"),
    "email":fields.String(required = False, description = "User Email", example = "User1@gmail.com")
})

UserResponseSchema = Model("UserResponseSchema", {
    "id": fields.Integer(readonly=True),
    "name": fields.String(),
    "email": fields.String(),
})

UserBooksRequestSchema = Model("UserBooksRequestSchema", {
    "title": fields.String(required = True, description="Book title"),
    "price": fields.Integer(required = True, description="Book price"),
    "user": fields.Integer(required = True, description="Author user ID")
})

UserBooksResponseSchema = Model("UserBooksResponseSchema", {
    "id": fields.Integer(readonly=True),
    "title": fields.String(),
    "price": fields.Integer(),
    "user_id": fields.Integer(attribute="user_id")
})

UserBooksUpdateModel = Model("UserBooksUpdateModel",{
    "id": fields.Integer(required = True, description = "Book id", example = 123),
    "title" : fields.String(required = False, description = "Book Title", example = "Harry Potter"),
    "price" : fields.Integer(required = False, description = "Book Price", example = 1000),
    "user_id" : fields.Integer(required = False, description = "Author Id", example = 1)
})

UserBookReturnModel = Model("UserBookModel",{
    "user_name": fields.String(attribute="user.name"),
    "books": fields.List(fields.Nested(UserBooksResponseSchema))
})

def register_user_models(ns):
    """
    Attach models to namespace with clean names.
    """
    ns.models[UserRequestSchema.name] = UserRequestSchema
    ns.models[UserResponseSchema.name] = UserResponseSchema
    ns.models[UserBooksRequestSchema.name] = UserBooksRequestSchema
    ns.models[UserBooksResponseSchema.name] = UserBooksResponseSchema
    ns.models[UserBooksUpdateModel.name] = UserBooksUpdateModel
    ns.models[UserUpdateSchema.name] = UserUpdateSchema
    ns.models[UserBookReturnModel.name] UserBookReturnModel


    ns.UserRequestSchema = UserRequestSchema
    ns.UserResponseSchema = UserResponseSchema
    ns.UserBooksRequestSchema = UserBooksRequestSchema
    ns.UserBooksResponseSchema = UserBooksResponseSchema
    ns.UserBooksUpdateModel = UserBooksUpdateModel
    ns.UserUpdateSchema = UserUpdateSchema
    ns.UserBookReturnModel = UserBookReturnModel
