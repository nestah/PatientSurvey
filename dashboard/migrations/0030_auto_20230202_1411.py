# Generated by Django 3.0.5 on 2023-02-02 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0029_auto_20230202_0950'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestQuestionnaire',
        ),
        migrations.AlterModelOptions(
            name='designations',
            options={'ordering': ['updated']},
        ),
        migrations.RemoveField(
            model_name='designations',
            name='date_added',
        ),
        migrations.AddField(
            model_name='designations',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterModelTable(
            name='designations',
            table='Designations',
        ),
    ]
