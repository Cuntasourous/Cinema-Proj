# Generated by Django 4.1.5 on 2023-01-31 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cine_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_list',
            name='poster',
            field=models.ImageField(upload_to='static/posters/'),
        ),
        migrations.AlterField(
            model_name='movie_list',
            name='wallpaper',
            field=models.ImageField(upload_to='static/wallpapers/'),
        ),
    ]
