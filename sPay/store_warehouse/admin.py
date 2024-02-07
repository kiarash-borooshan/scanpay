from django.contrib import admin
from .models import Store, Category2, Comment, Customer, Order, OrderItem, Credit


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


@admin.register(Order)
class CustomerDecore(admin.ModelAdmin):
    list_display = ("customer", "date_order", "complete", "transaction_id")


@admin.register(Customer)
class OrderDecore(admin.ModelAdmin):
    list_display = ("user", "name", "email")


@admin.register(OrderItem)
class OrderItemDecore(admin.ModelAdmin):
    list_display = ("product", "order", "quantity", "date_added")


@admin.register(Credit)
class CreditDecore(admin.ModelAdmin):
    list_display = ("customer", "order", "address", "date_added")
