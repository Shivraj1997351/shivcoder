# Generated by Django 3.2.6 on 2021-10-05 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='thumbnail.jpg', upload_to='thumbnail'),
        ),
    ]
