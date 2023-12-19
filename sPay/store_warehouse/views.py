from django.shortcuts import render, get_object_or_404
from .models import Store


def post_list(request):
    # list = get_object_or_404(Store)
    stor_list = Store.objects.all()
    return render(request,
                  "store_warehouse/list.html",
                  {"list": stor_list})


