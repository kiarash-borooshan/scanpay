from django.contrib import admin
from .models import Store, Category2, Comment


@admin.register(Store)
class StoreDecore(admin.ModelAdmin):
    list_display = ("name", "code")
    prepopulated_fields = {
        "slug": ("name", "code")
    }


@admin.register(Category2)
class CategoryDecor(admin.ModelAdmin):
    list_display = ("title", "slug")
    prepopulated_fields = {
        "slug": ("title", "slug")
    }


@admin.register(Comment)
class CommentDecore(admin.ModelAdmin):
    list_display = ("name", "email")
