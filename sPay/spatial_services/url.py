from . import views
from django.urls import path

app_name = "spatial_services"

urlpatterns = [
    path("", views.spatial_services, name="spatial_service"),
    path("find_route/", views.find_route, name="find_route"),
    path("find_store/", views.find_store, name="find_store"),
]