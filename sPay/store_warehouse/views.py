from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Store, Comment
from .forms import AddPostForm, CommentForm


def first_page(request):
    return render(request,
                  "store_warehouse/first_page.html")


def post_list(request):
    # list = get_object_or_404(Store)
    contact_list = Store.objects.all()
    pagination = Paginator(contact_list, 2)
    page_number = request.GET.get("page")
    page_obj = pagination.get_page(page_number)

    return render(request,
                  "store_warehouse/post_list.html",
                  {"list": page_obj})


# class PostList(ListView):
#     """ post list class """
#     model = Store
#     template_name = "store_warehouse/post_list.html"
#     context_object_name = "list"


# class PostDetail(DetailView):
#     model = Store
#     template_name = "store_warehouse/post_detail.html"
#     context_object_name = "p_d"


def post_detail(request, pk):
    p_d = Store.objects.get(id=pk)
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


# class Dashboard(ListView):
#     """ داشبورد مشابه پست لیست است. اما پست لیست قابلیت ویرایش و حذف ندارد """
#     model = Store
#     template_name = "store_warehouse/dashboard.html"
#     context_object_name = "list"

@login_required()
def dashboard(request):
    """ dashboard """
    """ داشبورد مشابه پست لیست است. قابلیت ویرایش و حذف  """
    # list = get_object_or_404(Store)
    contact_list = Store.objects.all()
    pagination = Paginator(contact_list, 2)
    page_number = request.GET.get("page")
    page_obj = pagination.get_page(page_number)

    return render(request,
                  "store_warehouse/dashboard.html",
                  {"list": page_obj})

@login_required()
def dashboard_post_detail(request, pk):
    """ """
    p_d = Store.objects.get(id=pk)
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
                  "store_warehouse/dashboard_post_detail.html",
                  c)


# def add_post(request):
#     if request.method == "POST":
#         form = AddPostForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#
#     else:
#         form = AddPostForm()
#
#     return render(request,
#                   "store_warehouse/add_post.html",
#                   {"form": form})


class AddPost(LoginRequiredMixin, CreateView):
    model = Store
    template_name = "store_warehouse/add_post.html"
    fields = ("scan_same_QR", "scan_QR", "image_front", "image_behind",
              "name", "code", "description", "link", "age", "box",
              "variety", "category", "category2", "price")
    success_url = reverse_lazy("store_warehouse:add_post")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPost(LoginRequiredMixin, UpdateView):
    # TODO: user and slug must exclude
    model = Store
    fields = "__all__"
    # exclude = ("user", "slug")
    template_name = "store_warehouse/post_edit.html"
    context_object_name = "p_d"


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Store
    template_name = "store_warehouse/post_delete.html"
    success_url = reverse_lazy("store_warehouse:post_list")


def search(request):
    if request.method == "GET":
        q = request.GET.get("search")
    blog_list = Store.objects.filter(name__icontains=q)
    return render(request,
                  "store_warehouse/post_list.html",
                  {"list": blog_list})

