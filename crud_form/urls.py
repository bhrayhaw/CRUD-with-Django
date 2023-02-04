from django.urls import path
from crud_form import views

app_name = "crud_form"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('musician_details/<pk>/', views.MusicianDetails.as_view(), name='musician_details'),
    path('create_musician/', views.CreateMusician.as_view(), name='create_musician'),
    # path('create_album/<pk>/', views.CreateAlbum.as_view(), name='create_album'),
]
