from django.shortcuts import render
from ninja import Router

from .schemas import VehiclesSchema

class VehiclesViews():
    router = Router()

    @router.post('/')
    def create(req, data: VehiclesSchema):
        data = data.dict()

        return {'result': 'vehicles'}

    @router.get('/')
    def viewAll(req):
        return {'result': 'vehicles'}

    @router.get('/me')
    def viewAllMe(req):
        return {'result': 'vehicles'}

    @router.get('/')
    def view(req):
        return {'result': 'vehicles'}

    @router.put('/')
    def update(req):
        return {'result': 'vehicles'}

    @router.get('/')
    def delete(req):
        return {'result': 'vehicles'}

    # images 
    @router.post('/images')
    def create_image(req):
        return {'result': 'vehicles'}

    @router.get('/images')
    def view_image(req):
        return {'result': 'vehicles'}

    @router.put('/images')
    def update(req):
        return {'result': 'vehicles'}

    @router.delete('/images')
    def delete(req):
        return {'result': 'vehicles'}


