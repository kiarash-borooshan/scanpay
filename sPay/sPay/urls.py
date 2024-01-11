from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# TODO logout failed


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("Account.url")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("store_warehouse.url")),
    path("spatial_services/", include("spatial_services.url")),
    path("social_media/", include("social_media.url")),
    path("git&blog/", include("gitAndBlog.url")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
