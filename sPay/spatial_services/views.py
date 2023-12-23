from django.shortcuts import render


def spatial_services(request):
    return render(request,
                  "spatial_services/spatial_services.html")


def find_route(request):
    return render(request,
                  "spatial_services/find_route.html")


def find_store(request):
    return render(request,
                  "spatial_services/find_store.html")