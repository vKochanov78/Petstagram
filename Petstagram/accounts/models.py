from enum import Enum
from django import forms
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models



def validate_only_alphabetical(value):
    pass

class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Hidden'

    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class PetstagramUser(auth_models.AbstractUser):
    first_name = models.CharField(max_length=30, validators=(MinLengthValidator(2), validate_only_alphabetical), null=True, blank=True)
    last_name = models.CharField(max_length=30, validators=(MinLengthValidator(2), validate_only_alphabetical),null=True, blank=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=Gender.choices(),null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    def get_user_name(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        elif self.first_name or self.last_name:
            return self.first_name or self.last_name
        else:
            return self.username

# Create your models here.


class UserEditForm(forms.ModelForm):
    class Meta:
        model = PetstagramUser
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture', 'gender')
        exclude = ('password', )
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'profile_picture': 'Image',
            'gender': 'Gender',
        }


