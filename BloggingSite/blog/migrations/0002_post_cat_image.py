# Generated by Django 4.1.7 on 2023-02-26 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cat_image',
            field=models.FileField(default='', upload_to='cat/images/'),
        ),
    ]
