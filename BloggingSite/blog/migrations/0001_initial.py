# Generated by Django 4.1.7 on 2023-02-19 06:43

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('Github', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=130)),
                ('timeStamp', models.DateTimeField(blank=True)),
                ('category', models.CharField(default='', max_length=59)),
                ('subcategory', models.CharField(default='', max_length=57)),
                ('image', models.FileField(default='', upload_to='post/images/')),
                ('overview', models.TextField()),
                ('post_desc', tinymce.models.HTMLField(default='0')),
            ],
        ),
        migrations.CreateModel(
            name='PostextraImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='post/images/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
        ),
    ]