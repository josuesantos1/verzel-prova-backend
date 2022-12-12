from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from ninja import Router

from .schemas import VehiclesSchema
from .models import Vehicles

class VehiclesViews():
    router = Router()

    @router.post('/')
    def create(request, data: VehiclesSchema):
        data = data.dict()

        vehicles = Vehicles(**data)
        vehicles.save()

        return model_to_dict(vehicles)

    @router.get('/')
    def viewAll(request):
        vehicles =  Vehicles.objects.all().order_by('price')
        vehicles =  [{'id': i.id, 'name': i.name, 'descriptions': i.description, 'brand': i.brand, 'price': i.price, 'sold': i.sold} for i in vehicles]

        return vehicles

    @router.get('/me')
    def viewAllMe(request):
        return {'result': 'vehicles'}

    @router.get('/{id}')
    def view(request, id):
        vehicle = get_object_or_404(Vehicles, id=id)
        return model_to_dict(vehicle)

    @router.put('/')
    def update(request):
        return {'result': 'vehicles'}

    @router.delete('/')
    def delete(request):
        return {'result': 'vehicles'}

    # images 
    @router.post('/images')
    def create_image(request):
        return {'result': 'vehicles'}

    @router.get('/images')
    def view_image(request):
        return {'result': 'vehicles'}

    @router.put('/images')
    def update(request):
        return {'result': 'vehicles'}

    @router.delete('/images')
    def delete(request):
        return {'result': 'vehicles'}


