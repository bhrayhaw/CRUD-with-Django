from django.contrib import admin
from crud_form.models import MusicianModel, AlbumModel

# Register your models here.
admin.site.register(MusicianModel)
admin.site.register(AlbumModel)