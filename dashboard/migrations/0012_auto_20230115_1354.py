# Generated by Django 3.0.5 on 2023-01-15 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20230113_1808'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionnaire',
            old_name='is_active',
            new_name='isActive',
        ),
    ]
