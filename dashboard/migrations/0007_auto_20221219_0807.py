# Generated by Django 3.0.5 on 2022-12-19 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_name_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Name',
            new_name='Designations',
        ),
    ]
