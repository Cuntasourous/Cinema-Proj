# Generated by Django 4.1.5 on 2023-02-03 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cine_app', '0015_userprofileinfo_portfolio_site'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='portfolio_site',
        ),
    ]
