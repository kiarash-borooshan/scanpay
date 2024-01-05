from django.conf import settings
from django.contrib.auth import logout

from . import views
from django.urls import path

app_name = "Account"

urlpatterns = [
    path("register/", views.Register.as_view(), name="register"),
    path("logout/", views.logout_view, name="logout"),
    # path("password_change/", views.password_change, name="password_change_done"),
    path("password_change/done/", views.password_change_done, name="password_change_done")
]

