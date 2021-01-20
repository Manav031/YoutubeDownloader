from django.shortcuts import render, HttpResponse, redirect
from pytube import YouTube
import os
# Create your views here.

url = ''

def yt_main(request):
    return render(request, 'index.html')

def yt_download(request):
    global url
    url = request.GET.get('url')
    yt = YouTube(url)
    stream = yt.streams
    res = []
    resolutions = []
    for i in stream:
        if "video" in str(i) and "mp4" in str(i):
            res.append(i.resolution)
    return render(request, 'download.html', {'res': res})

def compt(request, res):
    global url
    homedir = os.path.expanduser("~")
    dirs = homedir + "/Downloads"
    print(dirs)
    if request.method == 'POST':
        YouTube(url).streams.filter(res=res).first().download(homedir + '/Downloads')
        return HttpResponse('''download completed <a href={% url '' %}>Home</a>''')
    else:
        return HttpResponse('soory something went wrong')