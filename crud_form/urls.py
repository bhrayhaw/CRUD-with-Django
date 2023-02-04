from django.urls import path
from crud_form import views

app_name = "crud_form"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('musician_details/<pk>/', views.MusicianDetails.as_view(), name='musician_details'),
    path('create_musician/', views.CreateMusician.as_view(), name='create_musician'),
    path('create_album/<int:artist_id>/', views.CreateAlbum.as_view(), name='create_album'),
    path('update_musician/<pk>/', views.UpdateMusician.as_view(), name='update_musician'),
    path('delete_musician/<pk>/', views.DeleteMusician.as_view(), name='delete_musician'),
]
