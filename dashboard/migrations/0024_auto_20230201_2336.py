# Generated by Django 3.0.5 on 2023-02-01 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0023_auto_20230201_2332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionnaireapi',
            old_name='status',
            new_name='isActive',
        ),
    ]
