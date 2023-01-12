from django.urls import path
from crud_form import views



urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='form'),
    path('album_form/', views.album_form, name='album_form'),
    path('album_list/<int:artist_id>/', views.album_list, name='album_list'),
    path('update_artist/<int:artist_id>/', views.update_artist, name='update_artist'),
    path('update_album/<int:album_id>/', views.update_album, name='update_album'),
    path('delete_album/<int:album_id>/', views.delete_album, name='delete_album'),
    path('delete_artist/<int:artist_id>/', views.delete_artist, name='delete_artist'),

]
