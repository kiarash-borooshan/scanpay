from django.shortcuts import render


def video_call(request):
    return render(request,
                  "social_media/video_call.html")
