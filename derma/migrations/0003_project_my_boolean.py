# Generated by Django 4.2.2 on 2023-06-29 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('derma', '0002_remove_project_created_at_remove_project_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='my_boolean',
            field=models.BooleanField(default=False),
        ),
    ]
