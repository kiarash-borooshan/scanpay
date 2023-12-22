from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Store
from .forms import AddPost


def first_page(request):
    return render(request,
                  "store_warehouse/first_page.html")


def post_list(request):
    # list = get_object_or_404(Store)
    stor_list = Store.objects.all()
    return render(request,
                  "store_warehouse/post_list.html",
                  {"list": stor_list})


def post_detail(request, id_num):
    p_d = Store.objects.get(id=id_num)
    return render(request,
                  "store_warehouse/post_detail.html",
                  {"p_d": p_d})


def add_post(request):
    if request.method == "POST":
        form = AddPost(data=request.POST)
        if form.is_valid():
            form.save()

    else:
        form = AddPost()

    return render(request,
                  "store_warehouse_forms/add_post.html",
                  {"form": form})