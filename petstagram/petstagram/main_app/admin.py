from django.contrib import admin

from petstagram.main_app.models import Profile, Pet, PetsPhoto


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", 'email', 'gender')


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@admin.register(PetsPhoto)
class PetsPhotoAdmin(admin.ModelAdmin):
    pass