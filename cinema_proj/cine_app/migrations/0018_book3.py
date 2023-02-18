# Generated by Django 4.1.5 on 2023-02-14 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cine_app', '0017_book2'),
    ]

    operations = [
        migrations.CreateModel(
            name='book3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.CharField(max_length=100)),
                ('seats', models.IntegerField(default=1)),
                ('date', models.DateField(default='2023-01-01')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cine_app.timeslots')),
            ],
        ),
    ]