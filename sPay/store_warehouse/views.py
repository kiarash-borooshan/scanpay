from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Store, Comment
from .forms import AddPost, CommentForm


def first_page(request):
    return render(request,
                  "store_warehouse/first_page.html")


def post_list(request):
    # list = get_object_or_404(Store)
    stor_list = Store.objects.all()
    return render(request,
                  "store_warehouse/post_list.html",
                  {"list": stor_list})


def post_detail(request, id_num):
    p_d = Store.objects.get(id=id_num)
    cmnt = Comment.objects.all().filter(store=p_d)

    if request.method == "POST":
        cmnt_frm = CommentForm(data=request.POST)
        if cmnt_frm.is_valid():
            cd = cmnt_frm.cleaned_data
            new_name = cd["name"]
            new_email = cd["email"]
            new_message = cd["message"]

            new_comment = Comment(name=new_name,
                                  email=new_email,
                                  message=new_message,
                                  store=p_d)
            new_comment.save()

    else:
        cmnt_frm = CommentForm()

    c = {
        "p_d": p_d,
        "comment": cmnt,
    }

    return render(request,
                  "store_warehouse/post_detail.html",
                  c)


def add_post(request):
    if request.method == "POST":
        form = AddPost(data=request.POST)
        if form.is_valid():
            form.save()

    else:
        form = AddPost()

    return render(request,
                  "store_warehouse_forms/add_post.html",
                  {"form": form})
