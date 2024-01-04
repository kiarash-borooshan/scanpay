from . import views
from django.urls import path

app_name = "Account"

urlpatterns = [
    path("register/", views.Register.as_view(), name="register"),
    path("logout/", views.logout_view, name="logout"),
]

