from django.contrib import admin
from .models import Store


@admin.register(Store)
class StoreDecore(admin.ModelAdmin):
    list_display = ("name", "code")
    prepopulated_fields = {
        "slug": ("name", "code")
    }
