# Generated by Django 3.2.6 on 2021-11-16 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='user_id',
            field=models.TextField(),
        ),
    ]
