# Generated by Django 4.1.5 on 2023-02-03 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cine_app', '0007_book_date_book_seat_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateField(default='2023/3/2'),
        ),
    ]