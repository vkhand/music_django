from django.http import Http404
from django.http import HttpResponse
#shortcut to use template
from django.shortcuts import render
#to use template with render
#from django.template import loader 
from .models import Album

def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums' : all_albums}

    #render has inbuilt function for httpresponse and it returns the required httpresponse
    return render(request,'music/index.html',context)

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album doesn't exist")
    return render(request,'music/detail.html',{'album':album})
