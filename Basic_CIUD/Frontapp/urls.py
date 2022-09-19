
from django.contrib import admin
from django.urls import path
from Frontapp import views

app_name = "Frontapp"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view, name='home'),
    path('album_view/',views.album_view, name='album_view'),
    path('Musician_view/',views.Musician_view, name='Musician_view'),
    path('AlbumForm_view/',views.AlbumForm_view, name='AlbumForm_view'),
    path('musicianForm_view/',views.musicianForm_view, name='musicianForm_view'),
    path('MusicianDet/<int:musician_id>/',views.MusicianDet,name='MusicianDet'),
    path('Ed_musician/<int:musicianE_id>/',views.Ed_musician,name='Ed_musician'),
    path('Ed_album/<int:AlbumE_id>/',views.Ed_album,name='Ed_album'),
    path('deleteMusician/<int:musicianE_id>/',views.deleteMusician,name='deleteMusician'),
    path('deleteAlbum/<int:AlbumE_id>/',views.deleteAlbum,name='deleteAlbum'),

]
