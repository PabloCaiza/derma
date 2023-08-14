# Generated by Django 4.2.2 on 2023-06-29 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('derma', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='technology',
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
