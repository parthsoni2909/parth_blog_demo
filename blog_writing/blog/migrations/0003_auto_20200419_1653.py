# Generated by Django 3.0.5 on 2020-04-19 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='thumbnail1',
            field=models.ImageField(default='', upload_to='project_image'),
        ),
        migrations.AddField(
            model_name='blog',
            name='thumbnail2',
            field=models.ImageField(default='', upload_to='project_image'),
        ),
    ]
