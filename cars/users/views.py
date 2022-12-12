from ninja import Router

class UsersViews:

    router = Router()

    @router.post('/')
    def create(request):
        return {'message': 'created'}

    @router.get('/me')
    def view(request):
        return 'ola'

    @router.put('/me')
    def update(request):
        return {'message': 'updated'}

    @router.delete('/me')
    def delete(request): 
        return {'message': 'deleted'}

