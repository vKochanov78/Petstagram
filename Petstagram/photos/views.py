from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Petstagram.photos.models import Photo
from Petstagram.photos.forms import PhotoCreateForm, PhotoEditForm


# Create your views here.

@login_required
def add_photo(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        photo = form.save(commit=False)
        photo.user = request.user
        photo.save()
        return redirect('home-page')
    context = {'form': form}
    return render(request, 'photos/photo-add-page.html', context=context)


@login_required
def photo_details_page(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    context = {
        'photo': photo,
        'likes': likes,
        'comments': comments
    }
    return render(request, 'photos/photo-details-page.html', context=context)


@login_required
def photo_edit_page(request, pk):
    photo = Photo.objects.get(pk=pk)
    if request.method == 'GET':
        form = PhotoEditForm(instance=photo, initial=photo.__dict__)
    else:
        form = PhotoEditForm(request.POST, instance=photo)
        if form.is_valid():
            form.save()
        return redirect('photo-details-page', pk)
    context = {'form': form}
    return render(request, 'photos/photo-edit-page.html', context=context)


@login_required
def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('home-page')
