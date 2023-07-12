from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Pet
from .forms import PetForm, PetDeleteForm


# Create your views here.

@login_required
def pet_add_page(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        pet = form.save(commit=False)
        pet.user = request.user
        pet.save()
        return redirect('profile-details', pk=1)
    context = {'form': form}
    return render(request, 'pets/pet-add-page.html', context=context)


@login_required
def pet_details_page(request, username, pet_name):
    pet = Pet.objects.get(slug=pet_name)
    all_photos = pet.photo_set.all()
    context = {
        'pet': pet,
        'all_photos': all_photos
    }

    return render(request, 'pets/pet-details-page.html', context=context)


@login_required
def pet_edit_page(request, username, pet_name):
    pet = Pet.objects.get(slug=pet_name)
    if request.method == 'GET':
        form = PetForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet-details-page', username, pet_name)
    context = {'form': form}

    return render(request, 'pets/pet-edit-page.html', context=context)


@login_required
def pet_delete_page(request, username, pet_name):
    pet = Pet.objects.get(slug=pet_name)
    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=1)
    form = PetDeleteForm(initial=pet.__dict__)
    context = {'form': form}
    return render(request, 'pets/pet-delete-page.html', context=context)
