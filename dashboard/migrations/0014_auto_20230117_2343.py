# Generated by Django 3.0.5 on 2023-01-17 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_remove_questionnaire_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='number_of_questions',
            field=models.IntegerField(),
        ),
    ]
