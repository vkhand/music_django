from django.http import Http404
from django.http import HttpResponse
#shortcut to use template
from django.shortcuts import render, get_object_or_404
#to use template with render
#from django.template import loader 
from .models import Album

def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums' : all_albums}

    #render has inbuilt function for httpresponse and it returns the required httpresponse
    return render(request,'music/index.html',context)

def detail(request, album_id):
    # try:
    #     album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("Album doesn't exist")
    #shortcut for above try,except block is:
    album = get_object_or_404(Album, pk=album_id)
    return render(request,'music/detail.html',{'album':album})
    
def favourite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk= request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request,'music/detail.html',{
            'album':album,
            'error_message': "You didn't select a valid song",
            })
    else:
        selected_song.is_favourite = True
        selected_song.save()
        return render(request,'music/detail.html',{'album':album})





















