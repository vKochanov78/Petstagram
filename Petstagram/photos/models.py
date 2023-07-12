from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from Petstagram.pets.models import Pet
from .validators import image_size_validator_5mb
# Create your models here.

UserModel = get_user_model()

class Photo(models.Model):
    pet_image = models.ImageField(blank=False, null=False, validators=(image_size_validator_5mb,), upload_to='images')
    description = models.TextField(max_length=300, validators=(MinLengthValidator(10),), blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pets = models.ManyToManyField(Pet, blank=True)
    date_of_publication = models.DateField(auto_now=True)
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pk} - {self.pet_image}'


