# Generated by Django 3.0.5 on 2022-12-12 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Total_Users',
            new_name='Users',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='Total_Users',
            new_name='Users',
        ),
    ]
