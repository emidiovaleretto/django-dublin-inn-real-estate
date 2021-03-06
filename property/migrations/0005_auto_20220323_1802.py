# Generated by Django 3.2 on 2022-03-23 18:02

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20220314_0006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
            ],
        ),
        migrations.RemoveField(
            model_name='property',
            name='image',
        ),
        migrations.AddField(
            model_name='property',
            name='image',
            field=models.ManyToManyField(blank=True, to='property.Image'),
        ),
    ]
