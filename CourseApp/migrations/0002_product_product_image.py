# Generated by Django 3.1.6 on 2021-02-25 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
