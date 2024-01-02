from . import views
from django.urls import path

app_name = "store_warehouse"

urlpatterns = [
    path("", views.first_page, name="first_page"),
    path("post_list/", views.post_list, name="post_list"),
    # path("post_list/", views.PostList.as_view(), name="post_list"),
    path("post_detail/<int:pk>/", views.post_detail, name="post_detail"),
    # path("post_detail/<int:pk>/", views.PostDetail.as_view(), name="post_detail"),
    path("add_post/", views.add_post, name="add_post"),
    # path("add_post/", views.AddPost.as_view(), name="add_post"),
    path("<int:pk>/edit/", views.EditPost.as_view(), name="post_edit"),
    path("<int:pk>/DeletePost/", views.DeletePost.as_view(), name="DeletePost"),
    path("search/", views.search, name="search")
]
