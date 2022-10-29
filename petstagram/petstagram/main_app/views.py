from PIL import Image
from django.shortcuts import render, redirect

from petstagram.main_app.forms import ProfileForm
from petstagram.main_app.models import Profile, Pet, PetsPhoto


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]


def get_pets():
    pets = Pet.objects.all()

    if pets:
        return pets


def home_page(request):
    context = {
        'hidden_buttons': True,
    }
    return render(request, 'home_page.html', context)


def show_dashboard(request):
    profile = get_profile()
    pets_photo = PetsPhoto.objects.filter(tagged_pets__user=profile)

    context = {
        'pets_photo': pets_photo,
    }
    return render(request, 'dashboard.html', context)


def show_profile_details(request):
    profile = get_profile()
    pets = get_pets()
    total_pets_photo = len(PetsPhoto.objects.filter(tagged_pets__user=profile))
    total_likes = sum(pp.likes for pp in PetsPhoto.objects.filter(tagged_pets__user=profile))
    image = profile.picture

    context = {
        'profile': profile,
        "pets": pets,
        'total_pets_photo': total_pets_photo,
        'total_likes': total_likes,
        "image": image,
    }
    return render(request, "profile_details.html", context)


def delete_user(request, pk):
    profile = Profile.objects.get(id=pk)
    profile.delete()
    return redirect('home')


def create_profile(request):
    if request.method == "GET":
        form = ProfileForm()
        context = {
            'form': form
        }
        return render(request, 'create_profile.html', context)

