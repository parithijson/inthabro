import imp
from django.shortcuts import render
from pytube import YouTube as yt
from io import BytesIO

from django.http import HttpResponse

# Create your views here.


def home(request):
    if request.method == 'POST':
        request.session['link'] = request.POST.get('url')
        try:
            hello = yt(request.session['link']).streams.filter(
                progressive=True)

            url = yt(request.session['link'])
            print(hello)
            k = url.check_availability()

            print(k)
        except:
            return render(request, 'error.html')
        return render(request, 'download.html', {'hello': hello, 'url': url})

    return render(request, "home.html")


def download(request):
    if request.method == "POST":
        buffer = BytesIO()
        url = yt(request.session['link'])
        itag = request.POST.get('itag')
        print(itag)
        video = url.streams.get_by_itag(itag)
        video.stream_to_buffer(buffer)
        buffer.seek(0)
        response = HttpResponse(buffer, content_type='video/mp4')
        response['Content-Disposition'] = 'attachment; filename=my_video.mp4'
        return response
    return render(request, 'home.html')
