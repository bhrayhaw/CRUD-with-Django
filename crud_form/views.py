from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from crud_form.models import MusicianModel, AlbumModel
from crud_form import models
from crud_form import forms
from django.db.models import Avg

# Create your views here.
class IndexView(ListView):
    context_object_name = 'musician_list'
    model = models.MusicianModel
    template_name = 'list.html'

class MusicianDetails(DetailView):
    context_object_name = 'musician_details'
    model = models.MusicianModel
    template_name = 'album_list.html'

class CreateMusician(CreateView):
    fields = ('first_name', 'last_name', 'email', 'instrument')
    model = models.MusicianModel
    template_name = 'musician_form.html'
    
class UpdateMusician(UpdateView):
    model = models.MusicianModel
    fields = ['first_name', 'last_name', 'email', 'instrument']
    template_name = 'musician_form.html'

class DeleteMusician(DeleteView):
    context_object_name = 'musician'
    model = models.MusicianModel
    template_name = 'delete.html'
    success_url = reverse_lazy('crud_form:index')
class CreateAlbum(CreateView):
    context_object_name = 'album'
    model = models.AlbumModel
    fields = ('album_name', 'release_date', 'number_stars')
    template_name = 'album_form.html'

    def form_valid(self, form):
        form.instance.artist = MusicianModel.objects.get(id=self.kwargs['artist_id'])
        return super().form_valid(form)
class UpdateAlbum(UpdateView):
    model = models.AlbumModel
    fields = ['album_name', 'release_date', 'number_stars']
    template_name = 'update_album.html'

class DeleteAlbum(DeleteView):
    model = models.AlbumModel
    template_name = 'delete_album.html'
    success_url = reverse_lazy('crud_form:musician_details')

    def get_queryset(self):
        return self.model.objects.filter(artist=self.kwargs['artist_id'])
