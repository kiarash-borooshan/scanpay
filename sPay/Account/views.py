from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView


class Register(CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


def logout_view(request):
    logout(request)
    request.session.flush()
    request.user = AnonymousUser
    return redirect("store_warehouse:post_list")


def password_change_done(request):
    logout(request)
    request.session.flush()
    request.user = AnonymousUser
    return redirect("login")
