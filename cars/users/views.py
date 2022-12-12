import crypt

from ninja import Router
from django.forms.models import model_to_dict
from ninja.errors import HttpError

from .models import Users
from .schemas import UserSchema

class UsersViews:

    router = Router()

    @router.post('/')
    def create(request, data: UserSchema):
        user = data.dict()

        if Users.objects.filter(email=user['email']).exists():
            raise HttpError(400, 'already exists')
            
        user['password'] = crypt.crypt(user['email']) 
        users = Users(**user)
        users.save()

        return model_to_dict(users)

    @router.get('/me')
    def view(request):
        return 'ola'

    @router.put('/me')
    def update(request):
        return {'message': 'updated'}

    @router.delete('/me')
    def delete(request): 
        return {'message': 'deleted'}

