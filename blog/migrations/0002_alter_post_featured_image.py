# Generated by Django 3.2.25 on 2024-05-13 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(default='media/placeholder.png', upload_to='media/'),
        ),
    ]