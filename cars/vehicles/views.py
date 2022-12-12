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

    @router.get('/all')
    def viewAll(request):
        vehicles =  Vehicles.objects.all().order_by('price')
        vehicles =  [{'id': i.id, 'name': i.name, 'descriptions': i.description, 'brand': i.brand, 'price': i.price, 'sold': i.sold} for i in vehicles]

        return vehicles

    @router.get('/')
    def view(request, id):
        vehicle = get_object_or_404(Vehicles, id=id)
        return model_to_dict(vehicle)

    @router.put('/')
    def update(request, id, data: VehiclesSchema):
        vehicle = get_object_or_404(Vehicles, id=id)
        for attr, value in data.dict().items():
            setattr(vehicle, attr, value)

        vehicle.save()
        return model_to_dict(vehicle)

    @router.delete('/')
    def delete(request, id):
        vehicle = get_object_or_404(Vehicles, id=id)
        vehicle.delete()

        return {'message': "deleted"}

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


