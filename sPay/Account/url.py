from . import views
from django.urls import path

app_name = "Account"

urlpatterns = [
    path("register/", views.register, name="register")
]