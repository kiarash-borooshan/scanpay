from django.conf import settings
from django.contrib.auth import logout

from . import views
from django.urls import path

app_name = "Account"

urlpatterns = [
    path("register/", views.Register.as_view(), name="register"),
    path("logout/", views.logout_view, name="logout"),
]

