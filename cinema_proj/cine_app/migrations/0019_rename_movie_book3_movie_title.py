# Generated by Django 4.1.5 on 2023-02-14 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cine_app', '0018_book3'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book3',
            old_name='movie',
            new_name='movie_title',
        ),
    ]
