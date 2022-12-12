from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from vehicles.views import VehiclesViews

api = NinjaAPI()

api.add_router('/vehicles/', VehiclesViews.router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]
