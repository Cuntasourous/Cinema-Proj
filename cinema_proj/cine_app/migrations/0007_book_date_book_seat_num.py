# Generated by Django 4.1.5 on 2023-02-03 09:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cine_app', '0006_alter_book_timeslot_1_alter_book_timeslot_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='seat_num',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]