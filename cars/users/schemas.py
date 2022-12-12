from ninja import ModelSchema

from .models import Users

class UserSchema(ModelSchema):
    class Config:
        model = Users
        model_exclude = ['id']