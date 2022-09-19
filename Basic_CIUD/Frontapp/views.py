from django.shortcuts import render
from django.http import HttpResponse
from Frontapp.models import Musician, Album
from Frontapp import froms
from django.db.models import Avg


# Create your views here.

def home_view(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'title': 'Home ', 'musician_list': musician_list}
    return render(request, 'frontapp/home.html', context=diction)


def album_view(request):
    album_list = Album.objects.order_by('name')
    diction = {'title': 'Album ', 'album_list': album_list}
    return render(request, 'frontapp/Album.html', context=diction)


def Musician_view(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'title': 'Musician', 'musician_list': musician_list}
    return render(request, 'frontapp/musician.html', context=diction)


def AlbumForm_view(request):
    AForm = froms.AlbumForm()
    if request.method == "POST":
        AForm = froms.AlbumForm(request.POST)
        if AForm.is_valid():
            AForm.save(commit=True)
            return album_view(request)

    diction = {'title': 'Album form', 'AForm': AForm}
    return render(request, 'frontapp/albumForm.html', context=diction)


def musicianForm_view(request):
    MForm = froms.MusicianForm()
    if request.method == "POST":
        MForm = froms.MusicianForm(request.POST)
        if MForm.is_valid():
            MForm.save(commit=True)
            return home_view(request)
    diction = {'title': 'Musician form', 'MForm': MForm}
    return render(request, 'frontapp/musicianForm.html', context=diction)


def MusicianDet(request, musician_id):
    musicianD = Musician.objects.get(pk=musician_id)
    albumD = Album.objects.filter(artist=musician_id)
    albumDA = Album.objects.filter(artist=musician_id).aggregate(Avg('num_stars'))

    diction = {'title': 'Musician Detail', 'musicianD': musicianD, 'albumD': albumD, 'albumDA': albumDA}
    return render(request, 'frontapp/MusicianDet.html', context=diction)


def Ed_musician(request, musicianE_id):
    Ed_musicianList = Musician.objects.get(pk=musicianE_id)
    Muform = froms.MusicianForm(instance=Ed_musicianList)
    if request.method == "POST":
        Muform = froms.MusicianForm(request.POST, instance=Ed_musicianList)
        if Muform.is_valid():
            Muform.save(commit=True)
            return MusicianDet(request, musicianE_id)

    diction = {'title': 'Edit Musician', 'Muform': Muform}
    return render(request, 'frontapp/EditM.html', context=diction)


def Ed_album(request, AlbumE_id):
    EAinfo = Album.objects.get(pk=AlbumE_id)
    AEform = froms.AlbumForm(instance=EAinfo)
    if request.method == "POST":
        AEform = froms.AlbumForm(request.POST, instance=EAinfo)
        if AEform.is_valid():
            AEform.save(commit=True)
            return album_view(request)
    diction = {'title': 'Edit Musician', 'AEform': AEform}
    return render(request, 'frontapp/EditA.html', context=diction)


def deleteMusician(request, musicianE_id):
    DM_List = Musician.objects.get(pk=musicianE_id).delete()
    diction = {'title': 'Delete Musician', 'delete': 'Successfully Deleted'}
    return render(request, 'frontapp/delete.html', context=diction)


def deleteAlbum(request,AlbumE_id):
    DA_List = Album.objects.get(pk=AlbumE_id).delete()
    diction = {'title': 'Delete Album', 'delete': 'Successfully Deleted'}
    return render(request, 'frontapp/delete.html', context=diction)
