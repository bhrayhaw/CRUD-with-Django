from django.shortcuts import render, redirect
from crud_form.models import MusicianModel, AlbumModel
from crud_form import forms
from django.db.models import Avg

# Create your views here.
def home(request):
    musician_list = MusicianModel.objects.order_by('first_name')
    diction = {'musician_list': musician_list}
    return render(request, 'list.html', context=diction)

def album_list(request, artist_id):
    artist_info = MusicianModel.objects.get(pk=artist_id)
    album_list = AlbumModel.objects.filter(artist=artist_id)
    rating = AlbumModel.objects.filter(artist=artist_id).aggregate(Avg('number_stars'))
    diction = {'artist_info':artist_info,'album_list':album_list, 'artist_rating':rating}
    return render(request, 'album_list.html', context=diction)

def form(request):
    new_form = forms.MusicianForm()

    if request.method == 'POST':
        new_form = forms.MusicianForm(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)
            return home(request)
    diction = {'musician_form':new_form}
    return render(request, 'musician_form.html', context=diction)


def album_form(request):
    new_form = forms.AlbumForm()

    if request.method == 'POST':
        new_form = forms.AlbumForm(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)
            return home(request)
    diction = {'album_form':new_form}
    return render(request, 'album_form.html', context=diction)


#update artist info
def update_artist(request, artist_id):
    #get all artist data by id
    artist_info = MusicianModel.objects.get(pk=artist_id)
    #pass artist data into form fields
    new_form = forms.MusicianForm(instance=artist_info)

    if request.method == 'POST':
        new_form = forms.MusicianForm(request.POST, instance=artist_info)

        if new_form.is_valid():
            new_form.save(commit=True)
            return album_list(request, artist_id)

    diction={'artist_update':new_form}
    return render(request, 'update.html', context=diction)


#update album details
def update_album(request, album_id):
    album_info = AlbumModel.objects.get(pk=album_id)
    new_form = forms.AlbumForm(instance=album_info)
    diction={}

    if request.method == 'POST':
        new_form = forms.AlbumForm(request.POST, instance=album_info)

        if new_form.is_valid():
            new_form.save(commit=True)
            return redirect('album_list', album_info.artist.id)
    diction.update({'album_update':new_form})
    return render(request, 'update_album.html', context=diction)


#delete album records
def delete_album(album_id):
    album_info = AlbumModel.objects.get(pk=album_id)
    album_info.delete()
    return redirect('album_list', album_info.artist.id)

#delete artist records
def delete_artist(artist_id):
    artist_info = MusicianModel.objects.get(pk=artist_id)
    artist_info.delete()
    return redirect('home')