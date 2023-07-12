from django.contrib import admin
from .models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_publication', 'tagged_pet_str')

    @staticmethod
    def tagged_pet_str(obj):
        return ', '.join([pet.name for pet in obj.tagged_pets.all()])
# Register your models here.
