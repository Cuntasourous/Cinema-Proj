# Generated by Django 4.1.5 on 2023-02-03 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cine_app', '0011_alter_book_ticket_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='ticket_date',
            new_name='date',
        ),
    ]
