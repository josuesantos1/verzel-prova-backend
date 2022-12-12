from ninja import Schema

class VehiclesSchema(Schema):
    name: str
    brand: str
    description: str
    price: int
    sold: bool

# class UserSchema(ModelSchema):
#     class Config:
#         model = User
#         model_exclude = ['id']

class VehiclesImagesSchema(Schema):
    vehicles: int
    key: str
