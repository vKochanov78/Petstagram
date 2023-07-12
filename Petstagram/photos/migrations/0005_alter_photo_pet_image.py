# Generated by Django 4.2.1 on 2023-06-18 15:49

import Petstagram.photos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_alter_photo_pet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='pet_image',
            field=models.ImageField(upload_to='images', validators=[Petstagram.photos.validators.image_size_validator_5mb]),
        ),
    ]