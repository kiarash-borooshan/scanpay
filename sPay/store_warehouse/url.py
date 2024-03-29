from . import views
from django.urls import path

app_name = "store_warehouse"

urlpatterns = [
    path("", views.first_page, name="first_page"),
    path("guide", views.guide, name="guide"),
    path("post_list/", views.post_list, name="post_list"),
    # path("post_list/", views.PostList.as_view(), name="post_list"),
    path("post_detail/<int:pk>/", views.post_detail, name="post_detail"),
    # path("post_detail/<int:pk>/", views.PostDetail.as_view(), name="post_detail"),
    # path("add_post/", views.add_post, name="add_post"),
    path("add_post/", views.AddPost.as_view(), name="add_post"),
    path("<int:pk>/edit/", views.EditPost.as_view(), name="post_edit"),
    path("<int:pk>/DeletePost/", views.DeletePost.as_view(), name="DeletePost"),
    path("search/", views.search, name="search"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/post_detail/<int:pk>/", views.dashboard_post_detail, name="dashboard_post_detail"),
    path("cart/", views.cart, name="cart"),
    path("credit/", views.credit, name="credit"),
    path("update_item/", views.update_item, name="update_item")
]
