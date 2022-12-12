from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from vehicles.views import VehiclesViews
from users.views import UsersViews

api = NinjaAPI()

api.add_router('/vehicles/', VehiclesViews.router)
api.add_router('/users/', UsersViews.router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]
