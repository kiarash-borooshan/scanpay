from django.contrib import admin
from .models import Store, Category2, Comment


# class CommentInline(admin.StackedInline):
#     # TODO failed
#     """ show comment in admin """
#     model = Comment
#
#
# class StoreAdmin(admin.ModelAdmin):
#     inlines = [CommentInline]


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
    # list_display = ("writer", "email")
    list_display = ("name", "email")


# @admin.register(Cart)
# class CommentDecore(admin.ModelAdmin):
#     # list_display = ("writer", "email")
#     list_display = ("user", "product")
#
