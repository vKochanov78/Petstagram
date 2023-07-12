from django import forms
from Petstagram.photos.models import Photo


class PhotoCreateForm(forms.ModelForm):
    # user = forms.CharField(
    #     widget= forms.HiddenInput(),
    #     required=False,
    # )
    class Meta:
        model = Photo
        fields = '__all__'
        # widgets = {
        #     'user': forms.HiddenInput()
        # }

class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['pet_image']