from django.shortcuts import render


def git_blog(request):
    return render(request,
                  "gitBlog/gitBlog.html")
