# Generated by Django 4.1.5 on 2023-01-31 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=100, unique=True)),
                ('poster', models.ImageField(upload_to='media/posters/')),
                ('release_year', models.DateField()),
                ('runtime', models.DurationField()),
                ('rating', models.FloatField(max_length=3)),
                ('director', models.CharField(max_length=100)),
                ('age_restrict', models.CharField(max_length=5)),
                ('plot', models.TextField()),
                ('wallpaper', models.ImageField(upload_to='media/wallpapers/')),
                ('genre_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cine_app.genre')),
            ],
        ),
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeslot_1', models.CharField(max_length=10)),
                ('timeslot_2', models.CharField(blank=True, max_length=10)),
                ('timeslot_3', models.CharField(blank=True, max_length=10)),
                ('timeslot_4', models.CharField(blank=True, max_length=10)),
                ('movie_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cine_app.movie_list')),
            ],
        ),
    ]
