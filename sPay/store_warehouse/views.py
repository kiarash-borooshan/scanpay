from django.shortcuts import render, get_object_or_404
from .models import Store


def post_list(request):
    # list = get_object_or_404(Store)
    stor_list = Store.objects.all()
    return render(request,
                  "store_warehouse/list.html",
                  {"list": stor_list})


def post_detail(request, id_num):
    p_d = Store.objects.get(id=id_num)
    return render(request,
                  "store_warehouse/post_detail.html",
                  {"post_detail": p_d})